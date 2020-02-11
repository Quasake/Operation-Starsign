using UnityEngine;

public class Character : MonoBehaviour {
	public CharacterStat Health;
	public CharacterStat MysticPower;
	public CharacterStat Strength;
	public CharacterStat Defense;
	public CharacterStat MysticStrength;
	public CharacterStat Fortitude;
	public CharacterStat Speed;
	public CharacterStat Endurance;
	public CharacterStat Luck;
	public CharacterStat Charisma;

	[SerializeField] Inventory inventory;
	[SerializeField] Equipment equipment;
	[SerializeField] StatManager statManager;

	private void Awake ( ) {
		statManager.SetStats(Health, MysticPower, Strength, Defense, MysticStrength, Fortitude, Speed, Endurance, Luck, Charisma);
		statManager.UpdateStatValues( );

		inventory.OnItemRightClickedEvent += EquipFromInventory;
		equipment.OnItemRightClickedEvent += UnequipFromEquipmentPanel;
	}

	private void EquipFromInventory (Item item) {
		if (item is EquippableItem) {
			Equip((EquippableItem) item);
		}
	}

	private void UnequipFromEquipmentPanel (Item item) {
		if (item is EquippableItem) {
			Unequip((EquippableItem) item);
		}
	}

	public void Equip (EquippableItem item) {
		if (inventory.RemoveItem(item)) {
			EquippableItem previousItem;

			if (equipment.AddItem(item, out previousItem)) {
				if (previousItem != null) {
					inventory.AddItem(previousItem);

					previousItem.Unequip(this);
				}

				item.Equip(this);
				statManager.UpdateStatValues( );
			} else {
				inventory.AddItem(item);
			}
		}
	}

	public void Unequip (EquippableItem item) {
		if (!inventory.IsFull( ) && equipment.RemoveItem(item)) {
			inventory.AddItem(item);

			item.Unequip(this);
			statManager.UpdateStatValues( );
		}
	}
}
