using UnityEngine;

public class InventoryManager : MonoBehaviour {
	[SerializeField] Inventory inventory;
	[SerializeField] Equipment equipment;

	private void Awake ( ) {
		inventory.OnItemRightClickedEvent += Equip;
		equipment.OnItemRightClickedEvent += Unequip;
	}

	public void Equip (Item item) {
		if (inventory.RemoveItem(item)) {
			Item previousItem;

			if (equipment.AddItem(item, out previousItem)) {
				if (previousItem != null) {
					inventory.AddItem(previousItem);
				}
			} else {
				inventory.AddItem(item);
			}
		}
	}

	public void Unequip (Item item) {
		if (!inventory.IsFull( ) && equipment.RemoveItem(item)) {
			inventory.AddItem(item);
		}
	}
}
