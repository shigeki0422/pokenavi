package jp.pokenavi.app;

import android.app.Service;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.os.IBinder;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageButton;
import android.widget.LinearLayout;

public class FloatingWindowService extends Service {

    private WindowManager windowManager;
    private View floatingView;
    private WindowManager.LayoutParams params;

    private static final int COLLAPSED_SIZE = 120;   // dp: minimized button size
    private static final int EXPANDED_W = 360;        // dp
    private static final int EXPANDED_H = 600;        // dp
    private static final int HEADER_H = 56;           // dp: close button area

    private boolean isExpanded = false;

    @Override
    public IBinder onBind(Intent intent) { return null; }

    @Override
    public void onCreate() {
        super.onCreate();
        windowManager = (WindowManager) getSystemService(WINDOW_SERVICE);

        floatingView = buildView();

        params = new WindowManager.LayoutParams(
            dp(COLLAPSED_SIZE),
            dp(COLLAPSED_SIZE),
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            // FLAG_NOT_TOUCH_MODAL: touches OUTSIDE this window pass through to the app behind
            // FLAG_NOT_FOCUSABLE: don't steal keyboard focus
            WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
                | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS,
            PixelFormat.TRANSLUCENT
        );
        params.gravity = Gravity.TOP | Gravity.START;
        params.x = 50;
        params.y = 600;

        windowManager.addView(floatingView, params);
        showCollapsed();
    }

    private View buildView() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);

        // --- Collapsed button ---
        ImageButton btnExpand = new ImageButton(this);
        btnExpand.setImageResource(android.R.drawable.ic_menu_compass);
        btnExpand.setBackgroundColor(0xFF1a1a2e);
        btnExpand.setContentDescription("ポケナビを開く");
        LinearLayout.LayoutParams btnLp = new LinearLayout.LayoutParams(dp(COLLAPSED_SIZE), dp(COLLAPSED_SIZE));
        btnExpand.setLayoutParams(btnLp);
        btnExpand.setTag("btn_expand");
        root.addView(btnExpand);

        // --- Expanded panel ---
        LinearLayout panel = new LinearLayout(this);
        panel.setOrientation(LinearLayout.VERTICAL);
        panel.setVisibility(View.GONE);
        panel.setTag("panel");

        // Header with close button
        LinearLayout header = new LinearLayout(this);
        header.setBackgroundColor(0xFF1a1a2e);
        header.setGravity(Gravity.END);
        LinearLayout.LayoutParams headerLp = new LinearLayout.LayoutParams(
            WindowManager.LayoutParams.MATCH_PARENT, dp(HEADER_H));
        header.setLayoutParams(headerLp);

        ImageButton btnCollapse = new ImageButton(this);
        btnCollapse.setImageResource(android.R.drawable.ic_menu_close_clear_cancel);
        btnCollapse.setBackgroundColor(0x00000000);
        btnCollapse.setTag("btn_collapse");
        LinearLayout.LayoutParams closeLp = new LinearLayout.LayoutParams(dp(HEADER_H), dp(HEADER_H));
        btnCollapse.setLayoutParams(closeLp);
        header.addView(btnCollapse);
        panel.addView(header);

        // WebView
        WebView webView = new WebView(this);
        webView.setTag("webview");
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setLoadWithOverviewMode(true);
        ws.setUseWideViewPort(true);
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("https://pokenavi.jp");
        LinearLayout.LayoutParams wvLp = new LinearLayout.LayoutParams(
            WindowManager.LayoutParams.MATCH_PARENT, 0, 1f);
        webView.setLayoutParams(wvLp);
        panel.addView(webView);

        root.addView(panel);

        // --- Drag logic (applies to collapsed button) ---
        final int[] dragStart = new int[2];
        final int[] windowStart = new int[2];
        final boolean[] dragging = {false};

        btnExpand.setOnTouchListener((v, event) -> {
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
                        windowManager.updateViewLayout(floatingView, params);
                    }
                    return true;
                case MotionEvent.ACTION_UP:
                    if (!dragging[0]) showExpanded();
                    return true;
            }
            return false;
        });

        btnCollapse.setOnTouchListener((v, event) -> {
            if (event.getAction() == MotionEvent.ACTION_UP) {
                // Visual collapse only — NO updateViewLayout to avoid synthetic events
                isExpanded = false;
                floatingView.findViewWithTag("btn_expand").setVisibility(View.VISIBLE);
                floatingView.findViewWithTag("panel").setVisibility(View.GONE);
                // Resize after touch sequence is fully done (500ms > any touch debounce)
                floatingView.postDelayed(FloatingWindowService.this::finishCollapse, 500);
            }
            return true;
        });

        // Consume all touches that fall through (e.g., empty header area).
        // Prevents unhandled events from leaking to windows behind this overlay.
        root.setOnTouchListener((v, event) -> true);

        return root;
    }

    private void showCollapsed() {
        isExpanded = false;
        floatingView.findViewWithTag("btn_expand").setVisibility(View.VISIBLE);
        floatingView.findViewWithTag("panel").setVisibility(View.GONE);
        finishCollapse();
    }

    private void finishCollapse() {
        params.width = dp(COLLAPSED_SIZE);
        params.height = dp(COLLAPSED_SIZE);
        params.flags = WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL
            | WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
            | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS;
        windowManager.updateViewLayout(floatingView, params);
    }

    private void showExpanded() {
        isExpanded = true;
        floatingView.findViewWithTag("btn_expand").setVisibility(View.GONE);
        floatingView.findViewWithTag("panel").setVisibility(View.VISIBLE);

        params.width = dp(EXPANDED_W);
        params.height = dp(EXPANDED_H);
        // Expanded: FLAG_NOT_TOUCH_MODAL is intentionally ABSENT so the window
        // captures all touches within its bounds exclusively — prevents InputFlinger
        // from doing dual-dispatch to both this window and background windows.
        params.flags = WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
            | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS;
        windowManager.updateViewLayout(floatingView, params);
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
