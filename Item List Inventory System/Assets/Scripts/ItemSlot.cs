using UnityEngine;
using UnityEngine.UI;

public class ItemSlot : MonoBehaviour {
	public Inventory inventory;

	[SerializeField] Text ItemNameText;

	public void SetAsActiveSlot ( ) {
		if (!ItemNameText.text.Equals("")) {
			inventory.SetActiveSlot(this);
		}
	}

	public Item Item {
		get {
			return _item;
		}
		set {
			_item = value;

			if (_item != null) {
				ItemNameText.text = _item.ItemName;
			} else {
				ItemNameText.text = "";
			}
		}
	}

	private Item _item;
}
