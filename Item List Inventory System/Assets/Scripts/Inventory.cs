using System.Collections.Generic;
using UnityEngine;

public class Inventory : MonoBehaviour {
	public ItemSlot ActiveSlot;

	[SerializeField] Transform itemSlotsParent;
	[SerializeField] List<Item> items;
	[SerializeField] ItemSlot[ ] itemSlots;
	[Space]
	[SerializeField] Transform selector;

	private int page = 0;

	private void Start ( ) {
		SetActiveSlot(itemSlots[0]);
	}

	private void OnValidate ( ) {
		if (itemSlotsParent != null) {
			itemSlots = itemSlotsParent.GetComponentsInChildren<ItemSlot>( );
		}

		RefreshUI( );

		SetActiveSlot(itemSlots[0]);
	}

	private void RefreshUI ( ) {
		int i = page * itemSlots.Length;
		int k = 0;

		for (; i < items.Count && k < itemSlots.Length; i++, k++) {
			itemSlots[k].Item = items[i];
		}

		for (; k < itemSlots.Length; k++) {
			itemSlots[k].Item = null;
		}
	}

	public void SetActiveSlot (ItemSlot activeSlot) {
		ActiveSlot = activeSlot;

		Vector3 activeSlotPos = ActiveSlot.transform.localPosition;
		selector.localPosition = new Vector3(activeSlotPos.x - 275, activeSlotPos.y, selector.localPosition.z);
	}

	public void PageUp ( ) {
		if (page < items.Count / itemSlots.Length) {
			page++;

			RefreshUI( );
		}
	}

	public void PageDown ( ) {
		if (page > 0) {
			page--;

			RefreshUI( );
		}
	}

	public bool AddItem (Item item) {
		items.Add(item);
		RefreshUI( );

		return true;
	}

	public bool RemoveItem (Item item) {
		if (items.Remove(item)) {
			RefreshUI( );

			return true;
		}

		return false;
	}
}
