package com.bignerdranch.android.ponychat;

import android.app.ActionBar;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.net.wifi.WifiManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button joinBtn=(Button)findViewById(R.id.join_btn);
        Button createbtn = (Button)findViewById(R.id.create_btn);

        final WifiManager wifiMng = (WifiManager) getSystemService(Context.WIFI_SERVICE);


        joinBtn.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){

                wifiMng.setWifiEnabled(true);
            }
        });


    }



}
