```statblock
name: "ANGULOTL DAYBRINGER"
level: 1 
roles:
  - LEADER 
ancestry:
- Angulotl 
- Humanoid 
ev: 12 
stamina: 80 
immunities: poison 3 
speed: 5 (swim, climb) 
size: 1M / 
stability: 1 
free_strike: 4 
characteristics: 
  - +3 
  - +2 
  - 0 
  - +2 
  - 0 
actions:
  - name: "Acid Grasp"
    desc: "
      <br />**Type** Signature 
      <br />**Keywords** Melee, Strike, Weapon 
      <br />**Distance** Melee 1 
      <br />**Target** 2 creatures or objects 
      <br />`dice: 2d10 + 3` 
      <br />**✦ ≤11 7 acid damage; A< 1 dazed (save ends) 
      <br />**★ 12–16 10 acid damage; A< 2 dazed (save ends) 
      <br />**✸ 17 13 acid damage; A< 3 dazed (save ends) 
      <br />**Effect** The next time the target strikes the daybringer, they immediately take 4 acid damage. 
      <br />**1 Malice** The daybringer jumps 3 squares before or after using this ability."
maneuvers: 
  - name: "Sun Lamp"
    desc: "
      <br />**Keywords** — 
      <br />**Distance** Self 
      <br />**Target** Self 
      <br />**Effect** The daybringer expands their throat to resemble the sun until the start of their next turn. Each non-minion angulotl who starts their turn within 10 of the daybringer gains 5 temporary stamina and has their speed increased by 3 until the end of their turn."
ta:
  - name: "Tongue Slap"
    desc: "
      <br />**Keywords** — Distance Melee 5 
      <br />**Target** 1 creature 
      <br />**Trigger** The target targets the daybringer or an ally with a strike that isn’t a critical hit. 
      <br />**Effect** The daybringer reduces the power roll result by 1 tier. 
      <br />**2 Malice** Pull 4."
traits:
  - name: "Moisturizing End Effect"
    desc: "The daybringer either takes 5 damage or removes the wet effect from an adjacent creature and ends one save ends effect affecting them at the end of their turn."
va:
  - name: "New Dawn (Villain Action 1)" 
    desc: "
      <br />**Keywords** — 
      <br />**Distance** Ranged 10 
      <br />**Target** Special 
      <br />**Effect** Ten angulotl pollywogs escape the daybringer’s back and waddle into unoccupied squares within distance. "
  - name: "Plague of Frogs (Villain Action 2)" 
    desc: "
      <br />**Keywords** — 
      <br />**Distance** Self and 8 burst 
      <br />**Target** Self and all allies in the burst 
      <br />**Effect** Each target jumps 4 and makes a free strike."
  - name: "It Is Day (Villain Action 3)"
    desc: "
      <br />**Keywords** — 
      <br />**Distance** Special 
      <br />**Target** Special 
      <br />**Effect** The encounter map dries up and becomes illuminated. Each wet enemy has the wet condition end and takes 6 acid damage. All angulotls have a double edge on their next attack."
traits:
  - name: "Toxiferous"
    desc: "When an adjacent enemy grabs or uses a melee ability against the daybringer, they take 3 poison damage. "
```