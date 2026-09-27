package jp.pokenavi.app;

import android.app.Service;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.IBinder;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

public class FloatingWindowService extends Service {

    private WindowManager windowManager;
    private View floatingView;
    private WindowManager.LayoutParams params;

    private static final int COLLAPSED_SIZE = 56;
    private static final int FLOATING_W = 360;
    private static final int FLOATING_H = 600;
    private static final int HEADER_H = 48;
    private static final int FS_BAR_H = 32;

    private static final int MODE_COLLAPSED = 0;
    private static final int MODE_FLOATING = 1;
    private static final int MODE_FULLSCREEN = 2;

    private int mode = MODE_COLLAPSED;
    private int floatingX = 50;
    private int floatingY = 600;

    @Override
    public IBinder onBind(Intent intent) { return null; }

    @Override
    public void onCreate() {
        super.onCreate();
        windowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
        floatingView = buildView();
        params = new WindowManager.LayoutParams(
            dp(COLLAPSED_SIZE), dp(COLLAPSED_SIZE),
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS,
            PixelFormat.TRANSLUCENT
        );
        params.gravity = Gravity.TOP | Gravity.START;
        params.x = floatingX;
        params.y = floatingY;
        windowManager.addView(floatingView, params);
        applyMode(MODE_FLOATING);
    }

    private View buildView() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);

        // --- Collapsed bubble ---
        LinearLayout btnCollapsed = new LinearLayout(this);
        btnCollapsed.setOrientation(LinearLayout.VERTICAL);
        btnCollapsed.setGravity(Gravity.CENTER);
        btnCollapsed.setTag("btn_collapsed");
        GradientDrawable bubbleBg = new GradientDrawable();
        bubbleBg.setCornerRadius(dp(14));
        bubbleBg.setColor(0xFF1a1a2e);
        bubbleBg.setStroke(dp(2), 0xFF4a90e2);
        btnCollapsed.setBackground(bubbleBg);
        LinearLayout.LayoutParams bubbleLp = new LinearLayout.LayoutParams(dp(COLLAPSED_SIZE), dp(COLLAPSED_SIZE));
        btnCollapsed.setLayoutParams(bubbleLp);

        ImageView bubbleIcon = new ImageView(this);
        bubbleIcon.setImageResource(R.mipmap.ic_launcher_round);
        bubbleIcon.setScaleType(ImageView.ScaleType.FIT_CENTER);
        LinearLayout.LayoutParams iconLp = new LinearLayout.LayoutParams(dp(40), dp(40));
        bubbleIcon.setLayoutParams(iconLp);
        btnCollapsed.addView(bubbleIcon);

        root.addView(btnCollapsed);

        // --- Panel (shared by floating + fullscreen) ---
        LinearLayout panel = new LinearLayout(this);
        panel.setOrientation(LinearLayout.VERTICAL);
        panel.setVisibility(View.GONE);
        panel.setTag("panel");
        LinearLayout.LayoutParams panelLp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT,
            LinearLayout.LayoutParams.MATCH_PARENT
        );
        panel.setLayoutParams(panelLp);

        // Normal header (visible in MODE_FLOATING only)
        LinearLayout header = new LinearLayout(this);
        header.setBackgroundColor(0xFF1a1a2e);
        header.setGravity(Gravity.CENTER_VERTICAL);
        header.setTag("header");
        LinearLayout.LayoutParams headerLp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, dp(HEADER_H));
        header.setLayoutParams(headerLp);

        TextView title = new TextView(this);
        title.setText("ポケナビ");
        title.setTextColor(0xFF4a90e2);
        title.setTextSize(TypedValue.COMPLEX_UNIT_SP, 15);
        title.setTypeface(null, Typeface.BOLD);
        LinearLayout.LayoutParams titleLp = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f);
        titleLp.setMarginStart(dp(12));
        title.setLayoutParams(titleLp);
        header.addView(title);

        TextView btnMinimize = makeHeaderButton("−", "btn_minimize", HEADER_H);
        header.addView(btnMinimize);

        TextView btnFullscreen = makeHeaderButton("⛶", "btn_fullscreen", HEADER_H);
        header.addView(btnFullscreen);

        TextView btnClose = makeHeaderButton("✕", "btn_close", HEADER_H);
        header.addView(btnClose);

        panel.addView(header);

        // Fullscreen compact bar (visible in MODE_FULLSCREEN only)
        LinearLayout fsBar = new LinearLayout(this);
        fsBar.setBackgroundColor(0xCC1a1a2e);
        fsBar.setGravity(Gravity.CENTER_VERTICAL | Gravity.END);
        fsBar.setTag("fs_bar");
        fsBar.setVisibility(View.GONE);
        LinearLayout.LayoutParams fsBarLp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, dp(FS_BAR_H));
        fsBar.setLayoutParams(fsBarLp);

        TextView btnFsExit = makeHeaderButton("⊡", "btn_fs_exit", FS_BAR_H);
        fsBar.addView(btnFsExit);

        TextView btnFsClose = makeHeaderButton("✕", "btn_fs_close", FS_BAR_H);
        fsBar.addView(btnFsClose);

        panel.addView(fsBar);

        // WebView
        WebView webView = new WebView(this);
        webView.setTag("webview");
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setLoadWithOverviewMode(true);
        ws.setUseWideViewPort(true);
        webView.setBackgroundColor(0xFFFFFFFF);
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("https://pokenavi.jp");
        LinearLayout.LayoutParams wvLp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, 0, 1f);
        webView.setLayoutParams(wvLp);
        panel.addView(webView);

        root.addView(panel);

        // --- Touch listeners ---
        final int[] dragStart = new int[2];
        final int[] windowStart = new int[2];
        final boolean[] dragging = {false};

        btnCollapsed.setOnTouchListener((v, event) -> {
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    dragging[0] = false;
                    dragStart[0] = (int) event.getRawX();
                    dragStart[1] = (int) event.getRawY();
                    windowStart[0] = params.x;
                    windowStart[1] = params.y;
                    return true;
                case MotionEvent.ACTION_MOVE:
                    int dx = (int) event.getRawX() - dragStart[0];
                    int dy = (int) event.getRawY() - dragStart[1];
                    if (Math.abs(dx) > 8 || Math.abs(dy) > 8) dragging[0] = true;
                    if (dragging[0]) {
                        params.x = windowStart[0] + dx;
                        params.y = windowStart[1] + dy;
                        floatingX = params.x;
                        floatingY = params.y;
                        windowManager.updateViewLayout(floatingView, params);
                    }
                    return true;
                case MotionEvent.ACTION_UP:
                    if (!dragging[0]) applyMode(MODE_FLOATING);
                    return true;
            }
            return false;
        });

        btnMinimize.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) applyMode(MODE_COLLAPSED);
            return true;
        });

        btnFullscreen.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) returnToFullscreen();
            return true;
        });

        btnClose.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) stopSelf();
            return true;
        });

        btnFsExit.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) returnToFullscreen();
            return true;
        });

        btnFsClose.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) stopSelf();
            return true;
        });

        // Header drag (floating mode only)
        header.setOnTouchListener((v, event) -> {
            if (mode != MODE_FLOATING) return false;
            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    dragging[0] = false;
                    dragStart[0] = (int) event.getRawX();
                    dragStart[1] = (int) event.getRawY();
                    windowStart[0] = params.x;
                    windowStart[1] = params.y;
                    return true;
                case MotionEvent.ACTION_MOVE:
                    int dx = (int) event.getRawX() - dragStart[0];
                    int dy = (int) event.getRawY() - dragStart[1];
                    if (Math.abs(dx) > 8 || Math.abs(dy) > 8) dragging[0] = true;
                    if (dragging[0]) {
                        params.x = windowStart[0] + dx;
                        params.y = windowStart[1] + dy;
                        floatingX = params.x;
                        floatingY = params.y;
                        windowManager.updateViewLayout(floatingView, params);
                    }
                    return true;
                case MotionEvent.ACTION_UP:
                    return true;
            }
            return false;
        });

        root.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_OUTSIDE && mode == MODE_FLOATING) {
                applyMode(MODE_COLLAPSED);
            }
            return true;
        });

        return root;
    }

    private TextView makeHeaderButton(String text, String tag, int sizeDp) {
        TextView btn = new TextView(this);
        btn.setText(text);
        btn.setTextColor(0xFFCCCCCC);
        btn.setTextSize(TypedValue.COMPLEX_UNIT_SP, sizeDp == FS_BAR_H ? 15 : 18);
        btn.setGravity(Gravity.CENTER);
        btn.setTag(tag);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(dp(sizeDp), dp(sizeDp));
        btn.setLayoutParams(lp);
        return btn;
    }

    private void applyMode(int newMode) {
        if (newMode == MODE_FULLSCREEN) {
            floatingX = params.x;
            floatingY = params.y;
        }
        mode = newMode;

        View btnCollapsed = floatingView.findViewWithTag("btn_collapsed");
        View panel = floatingView.findViewWithTag("panel");
        View header = floatingView.findViewWithTag("header");
        View fsBar = floatingView.findViewWithTag("fs_bar");

        switch (mode) {
            case MODE_COLLAPSED:
                btnCollapsed.setVisibility(View.VISIBLE);
                panel.setVisibility(View.GONE);
                params.width = dp(COLLAPSED_SIZE);
                params.height = dp(COLLAPSED_SIZE);
                params.flags = WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                    | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                    | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS;
                params.x = floatingX;
                params.y = floatingY;
                windowManager.updateViewLayout(floatingView, params);
                break;

            case MODE_FLOATING:
                btnCollapsed.setVisibility(View.GONE);
                panel.setVisibility(View.VISIBLE);
                header.setVisibility(View.VISIBLE);
                fsBar.setVisibility(View.GONE);
                params.width = dp(FLOATING_W);
                params.height = dp(FLOATING_H);
                params.flags = WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS
                    | WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                    | WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH;
                params.x = floatingX;
                params.y = floatingY;
                windowManager.updateViewLayout(floatingView, params);
                break;

            case MODE_FULLSCREEN:
                btnCollapsed.setVisibility(View.GONE);
                panel.setVisibility(View.VISIBLE);
                header.setVisibility(View.GONE);
                fsBar.setVisibility(View.VISIBLE);
                params.width = WindowManager.LayoutParams.MATCH_PARENT;
                params.height = WindowManager.LayoutParams.MATCH_PARENT;
                params.flags = WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS;
                params.x = 0;
                params.y = 0;
                windowManager.updateViewLayout(floatingView, params);
                break;
        }
    }

    private void returnToFullscreen() {
        Intent intent = new Intent(this, MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        startActivity(intent);
        stopSelf();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (floatingView != null) windowManager.removeView(floatingView);
    }

    private int dp(int dp) {
        return (int) (dp * getResources().getDisplayMetrics().density);
    }
}
