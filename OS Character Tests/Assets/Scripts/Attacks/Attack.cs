using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public abstract class Attack {
	protected string name, desc;

	protected int dmg;
	protected float acc, dmgRat;

	protected int mpCost, bpCost, spCost;

	protected int[ ] attTypes;
	protected int dmgType, element;

	// Effect[] effects;

	#region Methods

	public void Perform (Creature[ ] attackers, Creature[ ] defenders) {
		/* Perform the attack and damage defenders */

		for (int i = 0; i < defenders.Length; i++) { // Loop through all defenders being affected by the attack
			float fullDmg = 0; // The full damage the defender will experience

			for (int j = 0; j < attackers.Length; j++) { // Loop through all the attackers that are attacking
				float Ac = CalculateAccuracyConstant(attackers[j], defenders[i]); // Calculate accuracy constant (hit or miss)
				float L = CalculateLuckModifier(attackers[j]); // Calculate luck
				float C = CalculateCharismaModifier(attackers[j]); // Calculate charisma
				float S = CalculateStaminaModifier(attackers[j]); // Calculate stamina
				float O = CalculateBonusModifier(attackers[j], defenders[i]); // Calculate bonuses
				float B = CalculateBaseDamage(attackers[j], defenders[i]); // Calculate base damage

				float D = Ac * Mathf.Round(((S * O * B) + C) * L); // Calculate the damage of the full attack

				fullDmg += D; // Add the calcualted damage to the total damage the defender will experience
				
				// attackers[j].SubtractStamina(CalculateStaminaLoss(attackers[j]));

				Debug.Log("Ac = " + Ac + ", L = " + L + ", B = " + B + ", S = " + S + ", C = " + C);
				Debug.Log("DAMAGE = " + D);
			}

			defenders[i].SubtractHealth(fullDmg); // Hit the defender for the full damage

			// *** RUN THROUGH EFFECTS AS WELL
		}
	}

	private float CalculateLuckModifier (Creature attacker) {
		/* Calculate the luck modifier for the damage formula */

		// Get a random number between 0 and 1, if that number is less than the characters luck, it is a crit attack
		return (Utils.GetRandDec(0, 1) <= attacker.GetLuck( )) ? Constants.CRIT : 1;
	}
	private float CalculateCharismaModifier (Creature attacker) {
		/* Calculate the charmisa modifier for the damage formula */

		if (dmgRat > 0) { // If the attack is physical
			float charRange = attacker.GetStrength( ) / 15f; // The full charisma range

			float minBound = -charRange + (attacker.GetCharisma( ) * charRange); // The minimum value based on charisma
			float maxBound = charRange - ((1 - attacker.GetCharisma( )) * charRange); // The maximum value based on charisma

			return Utils.GetRandDec(minBound, maxBound);
		}

		return 0;
	}
	private int CalculateAccuracyConstant (Creature attacker, Creature defender) {
		/* Calculate the accuracy constant for the damage formula */

		float boostRatio = attacker.GetAccuracyBoost( ) / defender.GetEvasionBoost( ); // The in-battle boost ratio between the attacker and the defender
		float speedRatio = attacker.GetSpeed( ) / defender.GetSpeed( ); // The speed ratio between the attacker and the defender

		// Get a random number between 0 and 1, if the number is less than the calcuated accuracy, it is a hit
		return (Utils.GetRandDec(0, 1) < boostRatio * speedRatio * acc) ? 1 : 0;
	}
	private float CalculateStaminaModifier (Creature attacker) {
		/* Calculate the stamina modifier for the damage formula */

		// 75 - 100 = 1
		// 50 - 75  = 0.75
		// 25 - 50  = 0.5
		// 0  - 25  = 0.25

		return 0.25f * Mathf.CeilToInt(attacker.GetStamina( ) / 25f);
	}
	private float CalculateBonusModifier (Creature attacker, Creature defender) {
		/* Calculate the bonuses for the damage formula */

		// DO THIS

		return 1;
	}
	private float CalculateBaseDamage (Creature attacker, Creature defender) {
		/* Calcuate the base damage of the attack for the damage formula */

		float attRatio = (attacker.GetStrength( ) * dmgRat) + (attacker.GetMysticStrength( ) * (1 - dmgRat)); // The ratio between the attackers attack stats
		float defRatio = (defender.GetDefense( ) * dmgRat) + (defender.GetFortitude( ) * (1 - dmgRat)); // The ratio between the defenders defense stats

		float fullDmg = dmg * (attRatio / defRatio);

		return (fullDmg < 0) ? 0 : fullDmg;
	}

	private float CalculateStaminaLoss (Creature attacker) {
		/* Caclulate the amount of stamina the attacker loses once the attack is complete */

		return spCost - (attacker.GetEndurance( ) / (2 * spCost));
	}

	#endregion

	#region Getters

	public string GetName ( ) {
		return name;
	}

	public string GetDescription ( ) {
		return desc;
	}

	public int GetDamage ( ) {
		return dmg;
	}

	public float GetAccuracy ( ) {
		return acc;
	}

	public float GetDamageRatio ( ) {
		return dmgRat;
	}

	public int GetMPCost ( ) {
		return mpCost;
	}

	public int GetBPCost ( ) {
		return bpCost;
	}

	public int GetSPCost ( ) {
		return spCost;
	}

	public int[ ] GetAttackTypes ( ) {
		return attTypes;
	}

	public int GetDamageType ( ) {
		return dmgType;
	}

	public int GetElement ( ) {
		return element;
	}

	#endregion
}