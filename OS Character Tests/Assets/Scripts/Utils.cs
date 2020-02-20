using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class Utils {
	public static int GetRandInt (int min, int max) {
		/* Generate a random integer between <min> and <max> */

		return Constants.RANDOM.Next(min, max);
	}

	public static float GetRandDec (float min, float max) {
		/* Generate a random decimal between <min> and <max> */

		return (float) (Constants.RANDOM.NextDouble( ) * (max - min)) + min;
	}
}
