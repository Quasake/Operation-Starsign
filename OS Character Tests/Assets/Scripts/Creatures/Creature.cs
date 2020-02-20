using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class Creature : MonoBehaviour {
	[Header("Creature")]
	[SerializeField] protected int level;
	[SerializeField] protected int exp;

	[Header("Stats")]
	[SerializeField] protected float hp;
	[SerializeField] protected float mp;
	[SerializeField] protected float bp;
	[SerializeField] protected float strength;
	[SerializeField] protected float defense;
	[SerializeField] protected float mysticStrength;
	[SerializeField] protected float fortitude;
	[SerializeField] protected float speed;
	[SerializeField] protected float endurance;
	[SerializeField] protected float luck;
	[SerializeField] protected float charisma;

	[Header("In-Battle Stats")]
	[SerializeField] protected float accBoost;
	[SerializeField] protected float evaBoost;
	[SerializeField] protected float sp;
	[SerializeField] protected float recovery;

	[Header("Element Stats")]
	[SerializeField] protected int[ ] elemWeak;
	[SerializeField] protected int[ ] elemStrength;

	protected Item[ ] weapons;
	protected Item[ ] armor;
	protected Item[ ] footwear;
	protected Item[ ] accessories;

	protected AttackHandler attackHandler;
	// protected Ability[] passAbilities;

	#region Unity Methods



	#endregion

	#region Methods

	public void PerformAttack (int id, Creature[ ] attackers, Creature[ ] defenders) {
		attackHandler.GetAttack(id).Perform(attackers, defenders);
	}

	public void AddStamina (float stamina) {
		sp += (int) stamina;
	}

	public void SubtractStamina (float stamina) {
		sp -= (int) stamina;
	}

	public void AddHealth (float health) {
		hp += (int) health;
	}

	public void SubtractHealth (float damage) {
		hp -= (int) damage;
	}

	#endregion

	#region Setters

	protected void SetAttackHandler (AttackHandler attackHandler) {
		this.attackHandler = attackHandler;
	}

	#endregion

	#region Getters

	public float GetEndurance ( ) {
		return endurance;
	}

	public float GetSpeed ( ) {
		return speed;
	}
	public float GetMysticStrength ( ) {
		return mysticStrength;
	}
	public float GetDefense ( ) {
		return defense;
	}
	public float GetFortitude ( ) {
		return fortitude;
	}
	public float GetEvasionBoost ( ) {
		return evaBoost;
	}
	public float GetAccuracyBoost ( ) {
		return accBoost;
	}
	public float GetLuck ( ) {
		return luck;
	}
	public float GetStrength ( ) {
		return strength;
	}
	public float GetCharisma ( ) {
		return charisma;
	}
	public float GetStamina ( ) {
		return sp;
	}
	public float GetHealth ( ) {
		return hp;
	}

	#endregion
}