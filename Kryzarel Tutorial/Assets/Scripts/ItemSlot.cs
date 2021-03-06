﻿using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using System;

public class ItemSlot : MonoBehaviour, IPointerClickHandler, IPointerEnterHandler, IPointerExitHandler {
	[SerializeField] Image Image;
	[SerializeField] Sprite DefaultSprite;
	[SerializeField] ItemToolTip itemToolTip;

	public event Action<Item> OnRightClickEvent;

	public Item Item {
		get {
			return _item;
		}
		set {
			_item = value;

			UpdateImage( );
		}
	}

	private Item _item;

	protected virtual void OnValidate ( ) {
		if (Image == null) {
			Image = GetComponent<Image>( );
		}

		if (itemToolTip == null) {
			itemToolTip = FindObjectOfType<ItemToolTip>( );
		}
	}

	protected void UpdateImage ( ) {
		if (_item == null) {
			if (DefaultSprite != null) {
				Image.sprite = DefaultSprite;
			} else {
				Image.enabled = false;
			}
		} else {
			Image.sprite = _item.Icon;
			Image.enabled = true;
		}
	}

	public void OnPointerClick (PointerEventData eventData) {
		if (eventData != null && eventData.button == PointerEventData.InputButton.Right) {
			if (Item != null && OnRightClickEvent != null) {
				OnRightClickEvent(Item);
			}
		}
	}

	public void OnPointerEnter (PointerEventData eventData) {
		if (Item is EquippableItem) {
			itemToolTip.ShowToolTip((EquippableItem) Item);
		}
	}

	public void OnPointerExit (PointerEventData eventData) {
		itemToolTip.HideToolTip( );
	}
}
