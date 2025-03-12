# HAG OF THE GREEN AND ROT
```statblock
name: "HAG OF THE GREEN AND ROT"
level: 3
roles:
  - SOLO
ancestry:
  - Fey
  - Hag
ev: 50
stamina: 300
speed: 5 (flying, hover)
size: 1L /
stability: 1
free_strike: 6
characteristics:
  - +2
  - +1
  - +1
  - +3
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The hag takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the hag can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the hag can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Supernatural Resistance"
    desc: "Magic and Psionic abilities used against the hag have a bane."
actions:
  - name: "Corrosive Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 corruption damage; A< 1 [[weakened]] (save ends)
      <br />★ 12–16 13 corruption damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 16 corruption damage; A< 3 [[weakened]] (save ends)"
  - name: "Soul Steal"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 cube within 1
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 corruption damage P< 1 4 corruption damage
      <br />★ 12–16 8 corruption damage; P< 2 5 corruption damage
      <br />✸ 17+ 10 corruption damage; P< 3 6 corruption damage 
      <br />**Effect:** This ability has an edge against creatures with a soul.
      <br />**3 Malice** The hag regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Shapeshifter"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The hag alters their body to become any size 1 creature, such as a house cat. If the hag uses this ability while outside of an enemy’s [[Line of Effect]], the hag is considered hidden. The hag can return to their original form as a free maneuver.
      <br />**5 Malice** The hag becomes a size 2 creature instead, such as a bear. While in this form, the distance of their melee abilities increases by 1 and deal an additional 4 damage."
ta:
  - name: "Turned Upside Down"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Trigger** A creature hits the hag with a melee strike.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 Slide 2; R< 1 slide is vertical
      <br />★ 12–16 Slide 3; R< 2 slide is vertical, [[restrained]] (EoT)
      <br />✸ 17+ Vertical slide 5; R< 3 [[restrained]] (EoT) 
      <br />**Effect:** A creature [[restrained]] by this ability that is force moved vertically is suspended in midair until the condition ends."
va:
  - name: "Snackies for Sweeties (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All creatures 
      <br />**Effect:** The hag A< 2 attaches an ornate explosive pastry to each target. Roll power at the end of the round, targeting each creature with a pastry attached to them.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 poison damage
      <br />★ 12–16 10 poison damage
      <br />✸ 17+ 13 poison damage 
      <br />**Special** A creature wearing a pastry or adjacent to a creature wearing a pastry can attempt a hard Might test to remove the pastry as a maneuver. On success, the pastry is destroyed without exploding. On failure, the hag rolls power for all pastries immediately."
  - name: "Animal Alacrity (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The hag shifts up to their speed before using this action, uses Corrosive Claws against each target of this ability, pushes each target 2 squares, and then shifts up to their speed again."
  - name: "Open the Oven (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 fire damage; A< 1 [[weakened]] (save ends)
      <br />★ 12–16 10 fire damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 13 fire damage; A< 3 [[weakened]] (save ends) 
      <br />**Effect:** The hag turns the affected area into a roiling oven. The hag deals an additional 5 damage on abilities that target creatures in the affected area."

```
