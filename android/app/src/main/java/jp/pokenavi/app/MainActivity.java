package jp.pokenavi.app;

import android.app.AlertDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.provider.Settings;
import android.view.Gravity;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;
import com.getcapacitor.BridgeActivity;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class MainActivity extends BridgeActivity {

    private static final int OVERLAY_PERMISSION_REQ_CODE = 1001;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        stopService(new Intent(this, FloatingWindowService.class));
        addFloatingHeaderButton();
        checkForUpdate();
    }

    private void addFloatingHeaderButton() {
        // アイコン + テキストの横並びボタン
        LinearLayout btn = new LinearLayout(this);
        btn.setOrientation(LinearLayout.HORIZONTAL);
        btn.setGravity(Gravity.CENTER_VERTICAL);

        GradientDrawable bg = new GradientDrawable();
        bg.setCornerRadius(dp(20));
        bg.setColor(0xE61a1a2e);
        bg.setStroke(dp(1), 0xFF4a90e2);
        btn.setBackground(bg);
        btn.setPadding(dp(10), dp(5), dp(12), dp(5));

        TextView icon = new TextView(this);
        icon.setText("⧉");
        icon.setTextColor(0xFF4a90e2);
        icon.setTextSize(14);
        icon.setPadding(0, 0, dp(4), 0);
        btn.addView(icon);

        TextView label = new TextView(this);
        label.setText("フローティング");
        label.setTextColor(0xFF4a90e2);
        label.setTextSize(11);
        label.setTypeface(null, Typeface.BOLD);
        label.setLetterSpacing(0.02f);
        btn.addView(label);

        FrameLayout.LayoutParams lp = new FrameLayout.LayoutParams(
            FrameLayout.LayoutParams.WRAP_CONTENT,
            FrameLayout.LayoutParams.WRAP_CONTENT
        );
        lp.gravity = Gravity.TOP | Gravity.END;
        // ステータスバー(約74px)+サイトヘッダーの縦中心に合わせる
        lp.topMargin = dp(14);
        lp.rightMargin = dp(56);

        btn.setOnClickListener(v -> onFloatingButtonClick());

        FrameLayout contentFrame = getWindow().getDecorView().findViewById(android.R.id.content);
        if (contentFrame != null) contentFrame.addView(btn, lp);
    }

    private void onFloatingButtonClick() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && !Settings.canDrawOverlays(this)) {
            showPermissionDialog();
        } else {
            startFloatingService();
            moveTaskToBack(true);
        }
    }

    private void showPermissionDialog() {
        new AlertDialog.Builder(this)
            .setTitle("フローティング機能について")
            .setMessage("ポケナビをフローティングウィンドウとして他のアプリの上に表示できます。\n\n利用するには「他のアプリの上に重ねて表示」の許可が必要です。次の画面でポケナビの許可をオンにしてください。")
            .setPositiveButton("許可する", (dialog, which) -> {
                Intent intent = new Intent(
                    Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                    Uri.parse("package:" + getPackageName())
                );
                startActivityForResult(intent, OVERLAY_PERMISSION_REQ_CODE);
            })
            .setNegativeButton("キャンセル", null)
            .show();
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        stopService(new Intent(this, FloatingWindowService.class));
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == OVERLAY_PERMISSION_REQ_CODE) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && Settings.canDrawOverlays(this)) {
                startFloatingService();
                moveTaskToBack(true);
            }
        }
    }

    private void checkForUpdate() {
        new Thread(() -> {
            try {
                URL url = new URL("https://pokenavi.jp/app-version.json");
                BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()));
                StringBuilder sb = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) sb.append(line);
                reader.close();

                JSONObject json = new JSONObject(sb.toString());
                int latest = json.getInt("versionCode");
                String message = json.optString("message", "新しいバージョンが利用可能です");
                int current = getPackageManager().getPackageInfo(getPackageName(), 0).versionCode;

                if (latest <= current) return;

                SharedPreferences prefs = getSharedPreferences("pokenavi", MODE_PRIVATE);
                if (prefs.getInt("skipped_version", 0) >= latest) return;

                new Handler(Looper.getMainLooper()).post(() ->
                    new AlertDialog.Builder(this)
                        .setTitle("アップデートのお知らせ")
                        .setMessage(message + "\n\nGoogle Playで最新版をダウンロードできます。")
                        .setPositiveButton("今すぐ更新", (d, w) -> {
                            Intent i = new Intent(Intent.ACTION_VIEW,
                                Uri.parse("https://play.google.com/store/apps/details?id=" + getPackageName()));
                            startActivity(i);
                        })
                        .setNegativeButton("後で", (d, w) ->
                            prefs.edit().putInt("skipped_version", latest).apply()
                        )
                        .show()
                );
            } catch (Exception ignored) {}
        }).start();
    }

    private void startFloatingService() {
        startService(new Intent(this, FloatingWindowService.class));
    }

    private int dp(int dp) {
        return (int) (dp * getResources().getDisplayMetrics().density);
    }
}
