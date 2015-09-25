package org.abridgegame.randomwords;

import android.test.ActivityInstrumentationTestCase2;

/**
 * This is a simple framework for a test of an Application.  See
 * {@link android.test.ApplicationTestCase ApplicationTestCase} for more information on
 * how to write and extend Application tests.
 * <p/>
 * To run this test, you can type:
 * adb shell am instrument -w \
 * -e class org.abridgegame.randomwords.WordsActivityTest \
 * org.abridgegame.randomwords.tests/android.test.InstrumentationTestRunner
 */
public class WordsActivityTest extends ActivityInstrumentationTestCase2<WordsActivity> {

    public WordsActivityTest() {
        super("org.abridgegame.randomwords", WordsActivity.class);
    }

}
