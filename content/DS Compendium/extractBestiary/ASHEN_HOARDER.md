# ASHEN HOARDER
```statblock
name: "ASHEN HOARDER"
level: 4
roles:
  - SOLO
ancestry:
  - Construct
  - Undead
ev: 60
stamina: 350
weaknesses: Holy 5
speed: 8 (burrow)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +4
  - -2
  - -2
  - +0
  - -5
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The ashen hoarder takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the ashen hoarder can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the ashen hoarder can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
actions:
  - name: "Claw and Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; one target M < 2 [[bleeding]] (save ends); other target A < 2 [[grabbed]]
      <br />★ 12–16 15 damage; one target M < 3 [[bleeding]] (save ends); other target A < 3 [[grabbed]]
      <br />✸ 17+ 18 damage; M < 4 [[bleeding]] (save ends); A < 4 [[grabbed]] 
      <br />**Effect:** The ashen hoarder can have up to two size 1 creatures [[grabbed]] at the same time."
  - name: "Corpse Bomb"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 4 cube within 20
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage; A < 2 [[weakened]] (save ends)
      <br />★ 12–16 8 damage; A < 3 [[weakened]] (save ends)
      <br />✸ 17+ 11 damage; A < 4 [[weakened]] (save ends) 
      <br />**3 Malice** The ashen hoarder targets a second 4 cube within distance. 
      <br />**2 Malice** An enemy [[weakened]] by a Corpse Bomb is also [[slowed]] (save ends)"
  - name: "Impale"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 4 x 1 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 corruption damage; M < 2 impaled (save ends)
      <br />★ 12–16 11 corruption damage; M < 3 impaled (save ends)
      <br />✸ 17+ 14 corruption damage; M < 4 impaled (save ends) 
      <br />**Effect:** An impaled creature is [[restrained]] and [[bleeding]] until the condition ends. Each impaled creature moves whenever the ashen hoarder moves. The ashen hoarder can have no more than 3 creatures impaled with this ability at a time. 
      <br />**2 Malice** A creature impaled by this ability can be used with the Armor of Corpses ability instead of paying Malice."
maneuvers:
  - name: "Bone Dozer"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The ashen hoarder moves up to twice their speed in a straight line. Each creature and object in the ashen hoarder’s way is either moved into the nearest unoccupied square to the side or M < 3 is pushed forward until the end of the ashen hoarder’s movement. A target that is force moved into an obstacle is [[dazed]] (save ends)."
ta:
  - name: "Armor of Corpses"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The ashen hoarder takes damage. 
      <br />**Effect:** The ashen hoarder halves the incoming damage. If an impaled creature was used in place of spending Malice on this ability, the impaled creature takes the other half of the damage."
traits:
  - name: "Unshackled Rage"
    desc: "The ashen hoarder is commanded by whoever holds its Soul Shackle. A Soul Shackle is a size 1T object with 5 stamina. If the Soul Shackle is destroyed, the ashen hoarder flies into an unshackled rage. While raging, the ashen hoarder has a double edge on their abilities, damage immunities 5, ignores all commands, and is hostile to all living creatures within [[Line of Effect]]. At the start of each of their turns, the ashen hoarder takes 10 damage that can’t be reduced."
  - name: "Bladed Body"
    desc: "Whenever an enemy makes physical contact with the ashen hoarder or uses a melee ability against the ashen hoarder, they take 3 damage."
  - name: "Soul Singularity"
    desc: "When the Ashen Hoarder is reduced to 0 stamina it explodes in a swirling singularity of bone shards and soul energy. Each creature within 5 takes M< 3 11 corruption damage. If a creature is killed by this explosion, their soul is sucked into the vortex and is lost somewhere on the plane of the dead. They cannot be resurrected until their soul is recovered."
va:
  - name: "Skeletal Eruption (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 8 x 3 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 damage, vertical push 2 straight upward
      <br />★ 12–16 11 damage, vertical push 3 straight upward
      <br />✸ 17+ 14 damage, vertical push 4 straight upward 
      <br />**Effect:** Each target that would normally fall [[prone]] is instead [[restrained]] (save ends)."
  - name: "Mobile Mine Field (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 10 cube within 20
      <br />**Target** Special 
      <br />**Effect:** The Ashen Hoarder sprays out a rain of zombie mines brimming with necrotic energy. Six size 1M zombie mines appear in unoccupied squares within distance. An enemy that moves into a square adjacent to a zombie mine or starts their turn there causes the zombie mine to explode, dealing 4 corruption damage to each creature adjacent to the mine. A zombie explosion can trigger other zombie mines adjacent to it to also explode. At the start of each of the ashen hoarders’s turns, each zombie mine can be moved 2 squares."
  - name: "Ossuary Assault (Villain Action 3)"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The Ashen Hoarder moves up to their speed and makes a Claw and Blade attack with a double edge against a single target. On a tier-3 result, the ashen hoarder then uses Impale without spending malice."

```
