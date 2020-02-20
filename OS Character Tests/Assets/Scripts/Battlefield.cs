using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Battlefield : MonoBehaviour {
	[SerializeField] Creature[ ] attackers;
	[SerializeField] Creature[ ] defenders;

	private void Start ( ) {
		for (int i = 0; i < attackers.Length; i++) {
			attackers[i].gameObject.transform.localPosition += Vector3.right * 3;
		}
		for (int i = 0; i < defenders.Length; i++) {
			defenders[i].gameObject.transform.localPosition += Vector3.left * 3;
		}
	}

	private void Update ( ) {
		if (Input.GetButtonDown("Attackbitch")) {
			attackers[0].PerformAttack(0, attackers, defenders);
		}
	}
}
