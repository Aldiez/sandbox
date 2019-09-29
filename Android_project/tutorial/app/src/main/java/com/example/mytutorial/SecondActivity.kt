package com.example.mytutorial

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import java.util.Random
import android.view.View
import android.widget.TextView
import org.w3c.dom.Text

class SecondActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)
        showRandomNumber()
    }

    companion object {
        const val TOTAL_COUNT = "total_count"
    }

    fun showRandomNumber() {
        // Get the count from the intent extras
        val count = intent.getIntExtra(TOTAL_COUNT, 0)

        // Generate the random number
        val random = Random()
        var randomInt = 0

        // Add one because the bound is exclusive
        if (count > 0) {
            // Add one because the bound is exclusive
            randomInt = random.nextInt(count + 1)
        }

        // Display the random number
        findViewById<TextView>(R.id.textview_random).text = Integer.toString(randomInt)

        // Substitute the max value into the string source
        // for the heading, and update the heading
        findViewById<TextView>(R.id.textview_label).text = getString(R.string.random_heading, count)
    }
}