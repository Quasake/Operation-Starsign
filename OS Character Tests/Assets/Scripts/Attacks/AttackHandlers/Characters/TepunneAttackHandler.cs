using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TepunneAttackHandler : AttackHandler {
	public TepunneAttackHandler ( ) : base( ) {
		AddAttack(new StaffParry( ));
	}
}

class StaffParry : Attack {
	public StaffParry ( ) : base( ) {
		name = "Staff Parry";
		desc = "The user parries an incoming physical attack with a staff, negating the damage and countering. The likelihood of a successful counter increases the faster the user is than the opponent.";

		dmg = 0; // ?
		acc = 0; // ?
		dmgRat = 1;

		mpCost = 0;
		bpCost = 0;
		spCost = 0; // ?

		attTypes = new int[ ] { Constants.ATT_TYPE_COUNTER, Constants.ATT_TYPE_PARRY };
		dmgType = Constants.DMG_TYPE_BASIC;
		element = Constants.ELEM_BASIC;
	}
}
