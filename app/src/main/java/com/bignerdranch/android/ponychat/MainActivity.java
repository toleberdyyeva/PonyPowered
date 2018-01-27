package com.bignerdranch.android.ponychat;

import android.app.ActionBar;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.net.wifi.p2p.WifiP2pManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private final IntentFilter intentFilter = new IntentFilter();

    WifiP2pManager.Channel mChannel;
    WifiP2pManager mManager;
    StringBuilder sb;
    List<ScanResult> wifiList;
    TextView mainText;
    WifiManager mainWifi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button joinBtn = (Button) findViewById(R.id.join_btn);
        Button createBtn = (Button) findViewById(R.id.create_btn);

        final WifiManager wifiMng = (WifiManager) getSystemService(Context.WIFI_SERVICE);

        mManager = (WifiP2pManager) getSystemService(Context.WIFI_P2P_SERVICE);
        mChannel = mManager.initialize(this, getMainLooper(), null);

        joinBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                wifiMng.setWifiEnabled(true);
            }
        });

        // Indicates a change in the Wi-Fi P2P status.
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_STATE_CHANGED_ACTION);

        // Indicates a change in the list of available peers.
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_PEERS_CHANGED_ACTION);

        // Indicates the state of Wi-Fi P2P connectivity has changed.
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION);

        // Indicates this device's details have changed.
        intentFilter.addAction(WifiP2pManager.WIFI_P2P_THIS_DEVICE_CHANGED_ACTION);


    }

    class WifiReceiver extends BroadcastReceiver {
        public void onReceive(Context c, Intent intent) {
            sb = new StringBuilder();
            mainWifi = (WifiManager) getSystemService(Context.WIFI_SERVICE);
            wifiList = mainWifi.getScanResults();
            for (int i = 0; i < wifiList.size(); i++) {
                sb.append(new Integer(i + 1).toString() + ".");
                sb.append((wifiList.get(i)).SSID);
                sb.append("\n");
            }
            mainText.setText(sb);


        }
    }
}
