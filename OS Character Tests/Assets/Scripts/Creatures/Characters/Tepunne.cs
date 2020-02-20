using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Tepunne : Character {
	public override void Awake ( ) {
		SetAttackHandler(new TepunneAttackHandler( ));
	}
}
