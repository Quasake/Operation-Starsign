using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class AttackHandler {
	List<Attack> attacks;

	public AttackHandler ( ) {
		attacks = new List<Attack>( );

		AddAttack(new BaseHit( ));
	}

	#region Methods

	protected void AddAttack (Attack attack) {
		attacks.Add(attack);
	}

	#endregion

	#region Getters

	public List<Attack> GetAttacks ( ) {
		return attacks;
	}

	public Attack GetAttack (int id) {
		if (id >= attacks.Count || id < 0) {
			return null;
		}

		return attacks[id];
	}

	#endregion
}
