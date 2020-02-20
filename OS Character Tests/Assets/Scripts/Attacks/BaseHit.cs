using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BaseHit : Attack {
	public BaseHit ( ) : base( ) {
		name = "Base Hit";
		desc = "Basic attack boiiii.";

		dmg = 10;
		acc = 1;
		dmgRat = 1;

		mpCost = 0;
		bpCost = 0;
		spCost = 1;

		attTypes = new int[ ] { Constants.ATT_TYPE_PHYSICAL };
		dmgType = Constants.DMG_TYPE_BASIC;
		element = Constants.ELEM_BASIC;
	}
}
