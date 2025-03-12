# SHADOW ELF ECLIPSE
```statblock
name: "SHADOW ELF ECLIPSE"
level: 6
roles:
  - LEADER
ancestry:
  - Fey
  - Shadow
  - Elf
ev: 32
stamina: 180
speed: 6 (climb)
size: 1M /
stability: 1
free_strike: 7
characteristics:
  - +4
  - +3
  - +2
  - +1
  - +2
actions:
  - name: "Manifold Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; I< 2 [[bleeding]] (save ends)
      <br />★ 12–16 16 damage; I< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 19 damage; I< 4 [[bleeding]] (save ends) 
      <br />**2 Malice** The potency of this ability increases by 1."
maneuvers:
  - name: "Grasping Shadow"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Three creatures or objects casting a shadow
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 pull 5; I< 2 [[slowed]] (save ends)
      <br />★ 12–16 pull 7; I< 3 [[slowed]] (save ends)
      <br />✸ 17+ pull 10; I< 4 [[slowed]] (save ends) 
      <br />**Effect:** The eclipse makes a free strike against each target pulled into an adjacent square."
ta:
  - name: "PUT IT OUT!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** An enemy uses an ability that emits light, such as fire. 
      <br />**Effect:** The enemy has a double bane on the ability. End 
      <br />**Effect:** At the end of their turn, the eclipse can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way. Of the Umbra The eclipse ignores concealment granted by darkness. While the eclipse is in direct sunlight, they have damage weakness 3. While the eclipse is concealed, they have damage immunity 3."
va:
  - name: "From the Shadows (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** All allies 
      <br />**Effect:** The eclipse calls forth one brush stalker that appears within distance. Each target then shifts up to their speed and makes a free strike."
  - name: "Cast Away All Hope (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The eclipse dispels their enemies’ hard  -earned advantages, removing each target’s surges. Each ally ignores edges and additional effects of each target’s damaging abilities until the end of the round."
  - name: "Umbral Hunger (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage 
      <br />**Effect:** R< 3 speed becomes zero (save ends). The affected area is shrouded in darkness and becomes concealment. When an enemy starts their turn in an affected square, they take 5 corruption damage."


```
