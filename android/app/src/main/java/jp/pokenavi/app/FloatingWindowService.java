package jp.pokenavi.app;

import android.app.AlertDialog;
import android.app.Service;
import android.content.Intent;
import android.content.res.Configuration;
import android.graphics.PixelFormat;
import android.graphics.Typeface;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.util.TypedValue;
import android.view.ContextThemeWrapper;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.TextView;
import org.json.JSONArray;

public class FloatingWindowService extends Service {

    private WindowManager wm;
    private View floatingView;
    private WindowManager.LayoutParams lp;
    private WebView webView;
    private String currentUrl = "https://pokenavi.jp";

    private static final int TAB_W    = 28;
    private static final int HANDLE_W = 20;
    private static final int HEADER_H = 48;
    private static final int DEFAULT_PANEL_W = 320;
    private static final int MIN_PANEL_W = 160;
    private static final int MAX_PANEL_W = 540;

    private static final int MODE_COLLAPSED = 0;
    private static final int MODE_FLOATING  = 1;
    private int mode = MODE_COLLAPSED;

    private int totalW;

    private boolean interactingWithWebView = false;

    private final Handler handler = new Handler(Looper.getMainLooper());
    private final Runnable restoreModal = () -> {
        interactingWithWebView = false;
        lp.flags |= WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                  | WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH;
        try { wm.updateViewLayout(floatingView, lp); } catch (Exception ignored) {}
    };

    @Override public IBinder onBind(Intent i) { return null; }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent != null) {
            String url = intent.getStringExtra("url");
            if (url != null && !url.isEmpty()) {
                currentUrl = url;
                if (webView != null) webView.loadUrl(url);
            }
        }
        return START_NOT_STICKY;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        wm = (WindowManager) getSystemService(WINDOW_SERVICE);
        totalW = dp(TAB_W + DEFAULT_PANEL_W + HANDLE_W);
        floatingView = buildView();
        lp = new WindowManager.LayoutParams(
            dp(TAB_W),
            WindowManager.LayoutParams.MATCH_PARENT,
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS
                | WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN,
            PixelFormat.TRANSLUCENT
        );
        lp.gravity = Gravity.TOP | Gravity.START;
        lp.x = 0;
        lp.y = 0;
        wm.addView(floatingView, lp);
        applyMode(MODE_FLOATING);
    }

    private View buildView() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.HORIZONTAL);

        // --- Tab (collapse / expand) ---
        LinearLayout tab = new LinearLayout(this);
        tab.setTag("tab");
        tab.setBackgroundColor(0xFF1a1a2e);
        tab.setGravity(Gravity.CENTER);
        tab.setOrientation(LinearLayout.VERTICAL);
        tab.setLayoutParams(new LinearLayout.LayoutParams(
            dp(TAB_W), LinearLayout.LayoutParams.MATCH_PARENT));
        TextView tabIco = new TextView(this);
        tabIco.setText("≡");
        tabIco.setTextColor(0xFF4a90e2);
        tabIco.setTextSize(TypedValue.COMPLEX_UNIT_SP, 14);
        tabIco.setGravity(Gravity.CENTER);
        tab.addView(tabIco);
        root.addView(tab);

        // --- Panel (header + webview) ---
        LinearLayout panel = new LinearLayout(this);
        panel.setTag("panel");
        panel.setOrientation(LinearLayout.VERTICAL);
        panel.setVisibility(View.GONE);
        panel.setLayoutParams(new LinearLayout.LayoutParams(
            0, LinearLayout.LayoutParams.MATCH_PARENT, 1f));

        LinearLayout header = new LinearLayout(this);
        header.setBackgroundColor(0xFF1a1a2e);
        header.setGravity(Gravity.CENTER_VERTICAL);
        header.setLayoutParams(new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, dp(HEADER_H)));
        TextView title = new TextView(this);
        title.setText("ポケナビ");
        title.setTextColor(0xFF4a90e2);
        title.setTextSize(TypedValue.COMPLEX_UNIT_SP, 15);
        title.setTypeface(null, Typeface.BOLD);
        LinearLayout.LayoutParams titleLp = new LinearLayout.LayoutParams(
            0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f);
        titleLp.setMarginStart(dp(10));
        title.setLayoutParams(titleLp);
        header.addView(title);
        header.addView(makeBtn("⛶", "btn_fs"));
        header.addView(makeBtn("✕", "btn_x"));
        panel.addView(header);

        webView = new WebView(this);
        webView.setTag("webview");
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setLoadWithOverviewMode(true);
        ws.setUseWideViewPort(true);
        webView.setBackgroundColor(0xFFFFFFFF);
        webView.addJavascriptInterface(new SelectBridge(), "_SB");
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView v, String url) {
                currentUrl = url;
                v.evaluateJavascript(
                    "(function(){" +
                    "var i=0;" +
                    "function setup(s){" +
                    "  if(s.dataset._sb)return;" +
                    "  s.dataset._sb=++i;" +
                    "  var sx,sy,mv;" +
                    "  s.addEventListener('touchstart',function(e){" +
                    "    sx=e.touches[0].clientX;sy=e.touches[0].clientY;mv=false;" +
                    "  },true);" +
                    "  s.addEventListener('touchmove',function(e){" +
                    "    if(Math.abs(e.touches[0].clientX-sx)>10||Math.abs(e.touches[0].clientY-sy)>10)mv=true;" +
                    "  },true);" +
                    "  s.addEventListener('touchend',function(e){" +
                    "    if(mv)return;" +
                    "    e.preventDefault();e.stopPropagation();" +
                    "    var opts=Array.from(s.options).map(function(o){return o.text;});" +
                    "    window._SB.show(s.dataset._sb,JSON.stringify(opts),s.selectedIndex);" +
                    "  },true);" +
                    "}" +
                    "document.querySelectorAll('select').forEach(setup);" +
                    "new MutationObserver(function(ms){ms.forEach(function(m){" +
                    "  m.addedNodes.forEach(function(n){" +
                    "    if(n.querySelectorAll)n.querySelectorAll('select').forEach(setup);" +
                    "  });" +
                    "})}).observe(document.documentElement,{childList:true,subtree:true});" +
                    "})();",
                    null
                );
            }
        });
        webView.loadUrl(currentUrl);
        webView.setLayoutParams(new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, 0, 1f));
        panel.addView(webView);
        root.addView(panel);

        // --- Resize handle (right edge) ---
        TextView handle = new TextView(this);
        handle.setTag("handle");
        handle.setBackgroundColor(0xFF2a2a4a);
        handle.setText("⋮");
        handle.setTextColor(0xFF4a90e2);
        handle.setGravity(Gravity.CENTER);
        handle.setVisibility(View.GONE);
        handle.setLayoutParams(new LinearLayout.LayoutParams(
            dp(HANDLE_W), LinearLayout.LayoutParams.MATCH_PARENT));
        root.addView(handle);

        // --- Touch listeners ---

        tab.setOnClickListener(v -> {
            if (mode == MODE_COLLAPSED) applyMode(MODE_FLOATING);
            else applyMode(MODE_COLLAPSED);
        });

        root.findViewWithTag("btn_fs").setOnTouchListener((v, e) -> {
            if (e.getAction() == MotionEvent.ACTION_UP) returnToFullscreen();
            return true;
        });
        root.findViewWithTag("btn_x").setOnTouchListener((v, e) -> {
            if (e.getAction() == MotionEvent.ACTION_UP) stopSelf();
            return true;
        });

        // Combo box fix: タッチ時に NOT_TOUCH_MODAL を外してポップアップを有効化、
        // 2秒無操作で復元
        webView.setOnTouchListener((v, e) -> {
            handler.removeCallbacks(restoreModal);
            interactingWithWebView = true;
            if ((lp.flags & WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL) != 0) {
                lp.flags &= ~(WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                            | WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH);
                wm.updateViewLayout(floatingView, lp);
            }
            if (e.getAction() == MotionEvent.ACTION_UP
                    || e.getAction() == MotionEvent.ACTION_CANCEL) {
                handler.postDelayed(restoreModal, 2000);
            }
            return false;
        });

        // Resize drag
        final int[] dragX = {0};
        final int[] startW = {0};
        handle.setOnTouchListener((v, e) -> {
            switch (e.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    dragX[0] = (int) e.getRawX();
                    startW[0] = totalW;
                    return true;
                case MotionEvent.ACTION_MOVE:
                    int delta = (int) e.getRawX() - dragX[0];
                    int newW = startW[0] + delta;
                    newW = Math.max(dp(TAB_W + MIN_PANEL_W + HANDLE_W),
                           Math.min(dp(TAB_W + MAX_PANEL_W + HANDLE_W), newW));
                    totalW = newW;
                    lp.width = totalW;
                    wm.updateViewLayout(floatingView, lp);
                    return true;
            }
            return false;
        });

        // Outside touch → フラグ復元 + コンボ操作中でなければ折りたたみ
        root.setOnTouchListener((v, e) -> {
            if (e.getAction() == MotionEvent.ACTION_OUTSIDE) {
                boolean wasInteracting = interactingWithWebView;
                handler.removeCallbacks(restoreModal);
                restoreModal.run();
                if (!wasInteracting) applyMode(MODE_COLLAPSED);
            }
            return false;
        });

        return root;
    }

    private class SelectBridge {
        @JavascriptInterface
        public void show(final String sbId, final String optionsJson, final int selectedIndex) {
            handler.post(() -> {
                try {
                    JSONArray arr = new JSONArray(optionsJson);
                    String[] items = new String[arr.length()];
                    for (int i = 0; i < arr.length(); i++) items[i] = arr.getString(i);
                    AlertDialog dialog = new AlertDialog.Builder(
                            new ContextThemeWrapper(FloatingWindowService.this,
                                    android.R.style.Theme_Material_Light_Dialog))
                            .setSingleChoiceItems(items, selectedIndex, (d, which) -> {
                                webView.evaluateJavascript(
                                    "(function(){" +
                                    "var s=document.querySelector('[data-_sb=\"" + sbId + "\"]');" +
                                    "if(s){s.selectedIndex=" + which + ";" +
                                    "s.dispatchEvent(new Event('change',{bubbles:true}));}" +
                                    "})();", null);
                                d.dismiss();
                            })
                            .setNegativeButton("キャンセル", null)
                            .create();
                    dialog.getWindow().setType(
                            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY);
                    dialog.show();
                } catch (Exception ignored) {}
            });
        }
    }

    private TextView makeBtn(String text, String tag) {
        TextView btn = new TextView(this);
        btn.setText(text);
        btn.setTag(tag);
        btn.setTextColor(0xFFCCCCCC);
        btn.setTextSize(TypedValue.COMPLEX_UNIT_SP, 18);
        btn.setGravity(Gravity.CENTER);
        btn.setLayoutParams(new LinearLayout.LayoutParams(dp(HEADER_H), dp(HEADER_H)));
        return btn;
    }

    private void applyMode(int newMode) {
        mode = newMode;
        View panel  = floatingView.findViewWithTag("panel");
        View handle = floatingView.findViewWithTag("handle");

        boolean isLandscape = getResources().getConfiguration().orientation
                == Configuration.ORIENTATION_LANDSCAPE;

        if (mode == MODE_COLLAPSED) {
            panel.setVisibility(View.GONE);
            handle.setVisibility(View.GONE);
            lp.width = dp(TAB_W);
            lp.height = WindowManager.LayoutParams.MATCH_PARENT;
            lp.flags = WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                     | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                     | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS
                     | WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN;
        } else {
            panel.setVisibility(View.VISIBLE);
            handle.setVisibility(View.VISIBLE);
            lp.width = totalW;
            // 横画面: 上下全画面 / 縦画面: 上部固定・画面の半分
            lp.height = isLandscape
                ? WindowManager.LayoutParams.MATCH_PARENT
                : getResources().getDisplayMetrics().heightPixels / 2;
            lp.flags = WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                     | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS
                     | WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN
                     | WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH;
        }
        lp.x = 0;
        lp.y = 0;
        wm.updateViewLayout(floatingView, lp);
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        if (mode == MODE_FLOATING) applyMode(MODE_FLOATING);
    }

    private void returnToFullscreen() {
        Intent intent = new Intent(this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        intent.putExtra("url", currentUrl);
        startActivity(intent);
        stopSelf();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        handler.removeCallbacksAndMessages(null);
        if (floatingView != null) {
            try { wm.removeView(floatingView); } catch (Exception ignored) {}
        }
    }

    private int dp(int dp) {
        return (int) (dp * getResources().getDisplayMetrics().density);
    }
}
