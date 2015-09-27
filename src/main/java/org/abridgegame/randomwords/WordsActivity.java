package org.abridgegame.randomwords;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.content.res.Resources;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;

import java.util.Random;

public class WordsActivity extends Activity
{
    private Random random;
    private String[] words;
    private String[] wikipedia;
    private TextView word;
    private TextView old;

    private int mAnimationDuration;

    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        random = new Random();
        Resources res = getResources();
        words = res.getStringArray(R.array.manywords);
        wikipedia = res.getStringArray(R.array.wikipedia);
        old = (TextView) findViewById(R.id.old_word_text);
        word = (TextView) findViewById(R.id.word_text);
        old.setVisibility(View.GONE);

        // Retrieve and cache the system's default "short" animation time.
        mAnimationDuration =
            res.getInteger(android.R.integer.config_longAnimTime);

        randomize(word);
    }

    /** Called when the user clicks the randomize button */
    public void randomize(View view) {
        // Pick a new random word!
        String w = "";
        if (random.nextInt(2) == 0) {
            int r = random.nextInt(words.length);
            w = words[r];
        } else {
            int r = random.nextInt(wikipedia.length);
            w = wikipedia[r];
        }
        TextView temp = old;
        old = word;
        word = temp;

        old.animate().alpha(0f)
            .rotation(70)
            .setDuration(mAnimationDuration)
            .translationY(150)
            .translationX(50)
            .setListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    old.setVisibility(View.GONE);
                }
            });

        word.setText(w);
        word.setAlpha(0f);
        word.setTranslationY(-100);
        word.setTranslationX(0);
        word.setRotation(0);
        word.setVisibility(View.VISIBLE);
        word.animate().alpha(1f)
            .translationY(0)
            .setDuration(2*mAnimationDuration).setListener(null);

    }
}
