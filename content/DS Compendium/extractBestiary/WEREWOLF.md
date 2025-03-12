# WEREWOLF
```statblock
name: "WEREWOLF"
level: 1
roles:
  - SOLO
ancestry:
  - Accursed
  - Humanoid
  - Werebeast
ev: 30
stamina: 200
speed: 8
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +3
  - +2
  - −1
  - +1
  - +1
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The werewolf takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the werewolf can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the werewolf can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Shapeshifter" 
    desc: "The werewolf enters combat in their hybrid humanoid form. Their shape can’t change via any effects beyond their own ability."
  - name: "Ferocity"
    desc: "The werewolf’s abilities are capable of inflicting ferocity points on non-stormwight enemies. If a creature has 10 or more ferocity at the start of their turn, they spend all their ferocity and either make a free strike at the nearest creature or shift up to their speed towards the nearest creature and take a free strike. Non-stormwight creatures that take damage in this way gain 1 ferocity. All accumulated ferocity disappears after completing a respite."
  - name: "Vukenstep"
    desc: "The werewolf ignores difficult terrain."
actions:
  - name: "Accursed Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; 2 ferocity
      <br />★ 12–16 13 damage; 4 ferocity
      <br />✸ 17+ 16 damage; 5 ferocity 
      <br />**2 Malice** The target has P< 0 lycanthropy. The potency of this attack increases by 1 each time the werewolf forces the same target to resist it. 
      <br />**Effect:** A creature afflicted with lycanthropy accumulates 2 ferocity at the end of each of their turns whenever they’re in combat. Their ferocity does not disappear after completing a respite; they must complete the Find a Cure project to end this condition."
  - name: "Claws"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 11 damage; 1 ferocity; M< 2 push 3
      <br />✸ 17+ 14 damage; 3 ferocity; M< 3 vertical slide 3"
  - name: "Berserker Slash"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf shifts up to their speed and uses Claws against each creature who comes within 1 of the werewolf during the move. The werewolf makes one power roll against all targets."
maneuvers:
  - name: "Wall Leap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf jumps 4 squares. If they end this movement at a wall, the werewolf jumps off the wall 4 squares and makes a melee free strike."
ta:
  - name: "Facepalm and Head Slam"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** — 
      <br />**Trigger** The target targets the werewolf with a melee ability after charging or moving 3 or more squares in a straight line towards them.
      <br />**Distance** Melee 1
      <br />**Target** 1 creature 
      <br />**Effect:** The target is knocked [[prone]] and takes 5 damage before executing the ability."
va:
  - name: "Howl (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11
      <br />**Target** moves up to their speed away from the werewolf; [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />`dice: 2d10 +
      <br />✦ 17+ no effect 
      <br />**Effect:** Enemies that have 1 or more ferocity gain 4 ferocity and howl along with the werewolf."
  - name: "Full Wolf (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf changes into a massive wolf, pushing adjacent creatures out of their way and moving into a square that can accommodate their new size:. Until they die or the end of the encounter, their speed is 10, their size is 3, and their stability is 2. Each of the werewolf’s strikes deal an additional 3 damage and inflict an additional 1 ferocity. The potency of the werewolf’s Accursed Bite increases by 1."
  - name: "Rampage (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** All creatures in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; 2 ferocity
      <br />★ 12–16 11 damage; 4 ferocity
      <br />✸ 17+ 14 damage; 8 ferocity; [[prone]] 
      <br />**Effect:** The werewolf shifts up to twice their speed either before or after using this ability."

```
