using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Character : Creature {
	public virtual void Awake ( ) {
		LoadCharacter( );
	}

	protected void LoadCharacter ( ) {
		// Load the stats from file
		// Load equipment
	}
}
