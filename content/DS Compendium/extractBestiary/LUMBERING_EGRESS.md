# LUMBERING EGRESS
```statblock
name: "LUMBERING EGRESS"
level: 6
roles:
  - LEADER
ancestry:
  - Abyssal
  - Demon
ev: 32
stamina: 180
weaknesses: Holy 5
speed: 6
size: 3 /
stability: 3
free_strike: 7
characteristics:
  - +4
  - -1
  - +1
  - +2
  - +2
actions:
  - name: "Ensnarer Cannon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creature or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 corruption damage; A<  2 [[restrained]] (save ends)
      <br />★ 12–16 16 corruption damage; A<  3 [[restrained]] (save ends)
      <br />✸ 17+ 19 corruption damage; A<  4 [[restrained]] (save ends) 
      <br />**2 Malice** An ensnarer(s) survives the launch, appearing adjacent to one of the targets. Two ensnarers appear on a tier-3 result."
maneuvers:
  - name: "Demonic Egress"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** 3 burst
      <br />**Target** Special 
      <br />**Effect:** Four level 1 demon minions (ensnarer, frenzied, pitling) burst forth from the egress and appear in unoccupied squares. 
      <br />**2 Malice** A level 4 demon minion (orflig, wobalas, grulqin) also bursts forth and appears in an unoccupied square."
  - name: "Abyssal Protectors"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** 5 burst
      <br />**Target** Special 
      <br />**Trigger** The last ally minion on the encounter map dies OR the Egress falls below 25 stamina. 
      <br />**Effect:** A muceron and 2 ensnarers appear anywhere in range. 
      <br />**End Effect:** At the end of their turn, the egress can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Soulsight"
    desc: "Each creature within 2 of the egress can’t be hidden from them."
va:
  - name: "Frenzied Deluge (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage; a frenzied appears in an unoccupied square adjacent to the target"
  - name: "Fold Space (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Self 
      <br />**Effect:** The egress folds into their own portal and teleports to an unoccupied space within distance. Four level 1 demon minions (ensnarer, frenzied, pitling) appear in the space the egress leaves behind."
  - name: "Blood of the Abyss (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 × 3 line within 1Target All enemies and objects in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 corruption damage; R<  2 [[weakened]] (save ends)
      <br />★ 12–16 10 corruption damage; R<  3 [[weakened]] (save ends)
      <br />✸ 17+ 13 corruption damage; R<  4 [[weakened]] (save ends) 
      <br />**Effect:** The egress recalls and instantly destroys any ally minions on the encounter map. A torrent of churned up minion bodies and blood erupts from the egress, dealing an additional 2 damage for each minion destroyed this way."

```
