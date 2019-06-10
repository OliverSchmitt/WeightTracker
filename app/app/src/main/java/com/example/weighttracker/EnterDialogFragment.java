package com.example.weighttracker;

import android.app.Dialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.Snackbar;
import android.support.v4.app.DialogFragment;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.AppCompatEditText;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class EnterDialogFragment extends DialogFragment {
    String TAG = "EnterDialogFragment";

    MainActivity activity;

    @NonNull
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        activity = (MainActivity) getActivity();

        AlertDialog.Builder builder = new AlertDialog.Builder(activity);
        final LayoutInflater inflater = requireActivity().getLayoutInflater();
        final View enterLayout = inflater.inflate(R.layout.dialog_enter, null);
        builder.setView(enterLayout)
                .setPositiveButton(R.string.ok, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        System.out.println("Positive button clicked");

                        RequestQueue queue = Volley.newRequestQueue(Objects.requireNonNull(getActivity()));
                        String url = "http://10.0.2.2:5000/weight_entered";

                        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
                                new Response.Listener<String>() {
                                    @Override
                                    public void onResponse(String response) {
                                        Log.d(TAG, "onResponse: Response received");
                                        Snackbar sent = Snackbar.make(activity.findViewById(android.R.id.content), R.string.sent, Snackbar.LENGTH_SHORT);
                                        sent.show();
                                    }
                                }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                Log.d(TAG, "onErrorResponse: Error " + error.toString());
                            }
                        }) {
                            @Override
                            protected Map<String, String> getParams() {
                                Map<String, String>  params = new HashMap<>();
                                AppCompatEditText input = enterLayout.findViewById(R.id.enterEditText);
                                String weight = Objects.requireNonNull(input.getText()).toString();
                                params.put("weight", weight);

                                return params;
                            }
                        };

                        queue.add(stringRequest);
                    }
                })
                .setNegativeButton(R.string.cancel, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        System.out.println("Negative button clicked");
                    }
                });
        return builder.create();
    }

}
