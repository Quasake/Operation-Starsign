using System;
using UnityEngine;

public class Equipment : MonoBehaviour {
	[SerializeField] Transform equipmentSlotsParent;
	[SerializeField] EquipmentSlot[ ] equipmentSlots;

	public event Action<Item> OnItemRightClickedEvent;

	private void Awake ( ) {
		for (int i = 0; i < equipmentSlots.Length; i++) {
			equipmentSlots[i].OnRightClickEvent += OnItemRightClickedEvent;
		}
	}

	private void OnValidate ( ) {
		equipmentSlots = equipmentSlotsParent.GetComponentsInChildren<EquipmentSlot>( );
	}

	public bool AddItem (Item item, out Item previousItem) {
		for (int i = 0; i < equipmentSlots.Length; i++) {
			if (equipmentSlots[i].EquipmentType == item.EquipmentType) {
				previousItem = equipmentSlots[i].Item;
				equipmentSlots[i].Item = item;

				return true;
			}
		}

		previousItem = null;

		return false;
	}

	public bool RemoveItem (Item item) {
		for (int i = 0; i < equipmentSlots.Length; i++) {
			if (equipmentSlots[i].Item == item) {
				equipmentSlots[i].Item = null;

				return true;
			}
		}

		return false;
	}
}
