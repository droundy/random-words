package org.abridgegame.randomwords;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.util.Random;

public class WordsActivity extends Activity
{
    private Random random;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        random = new Random();
        randomize(findViewById(R.id.word_text));
    }

    /** Called when the user clicks the randomize button */
    public void randomize(View view) {
        // Pick a new random word!
        TextView text = (TextView) findViewById(R.id.word_text);
        int r = random.nextInt(100);
        text.setText("Random " + r);
    }
}
