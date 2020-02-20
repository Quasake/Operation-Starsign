using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Anabelle : Character {
	public override void Awake ( ) {
		SetAttackHandler(new AnabelleAttackHandler( ));
	}
}
