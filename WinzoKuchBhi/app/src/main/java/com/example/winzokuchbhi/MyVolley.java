package com.example.winzokuchbhi;

import android.content.Context;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;

/**
 * Created by Junaid.Alam on 10/19/2019.
 */
public class MyVolley
{
    private static MyVolley mInstance;
    private static Context mCtx;
    private RequestQueue requestQueue;

    private MyVolley(Context context)
    {
        mCtx = context;
        requestQueue = getReqeustQueue();
    }

    private RequestQueue getReqeustQueue()
    {
        if(requestQueue==null)
        {
            requestQueue = Volley.newRequestQueue(mCtx.getApplicationContext());
        }
        return requestQueue;
    }

    public static synchronized MyVolley getmInstance(Context context)
    {
        if(mInstance==null)
        {
            mInstance =  new MyVolley(context);
        }
        return mInstance;
    }

    public<T> void addToRequestQueue(Request<T> request)
    {
        getReqeustQueue().add(request);
    }
}