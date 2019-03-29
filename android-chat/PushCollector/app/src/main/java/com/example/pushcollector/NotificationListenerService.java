package com.example.pushcollector;

import android.app.Notification;
import android.os.Bundle;
import android.service.notification.StatusBarNotification;
import android.util.Log;

import com.example.http.NetRetrofit;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class NotificationListenerService extends android.service.notification.NotificationListenerService {

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        Notification notification = sbn.getNotification();
        Bundle extras = notification.extras;
        String title = extras.getString(Notification.EXTRA_TITLE);
        CharSequence text = extras.getCharSequence(Notification.EXTRA_TEXT);
        CharSequence subText = extras.getCharSequence(Notification.EXTRA_SUB_TEXT);
        String packageName = sbn.getPackageName();
        if( (text != null &&
                "com.kakao.talk".equals(packageName)) ||
                (title != null &&
                    !title.equals("텔레그램") &&
                    "org.telegram.messenger".equals(packageName))){
            sendData(packageName + "||" + title + "||" + text + "||" + subText);
        }
    }

    private void sendData(String data){
        Call<String> res = NetRetrofit.getInstance().getService().sendData(data);
        res.enqueue(new Callback<String>() {
            @Override
            public void onResponse(Call<String> call, Response<String> response) {
//                Log.d("Retrofit", response.toString());
            }

            @Override
            public void onFailure(Call<String> call, Throwable t) {
                Log.e("Err", t.getMessage());
            }
        });

    }
}
