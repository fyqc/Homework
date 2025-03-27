### ATA 45 - Central Maintenance Computer System (CMCF)

1. **The Low Range Radio Altimeter system fails and the fault data goes to the primary display system and CMCF. What process does the CMCF perform with this information?**  
   The Central Maintenance Computing Function (CMCF) receives the fault data, logs it into its fault history database, and correlates it with other system data to determine the root cause and affected systems. It then generates a maintenance message or fault report, which can be accessed by maintenance personnel via the onboard maintenance system for troubleshooting and repair planning.

2. **A sensor has a fault and sends data to the CMCF. There is no flight deck effect (FDE). The CMCF shows a:**  
   The CMCF will display a maintenance message or status indication, typically classified as a “no dispatch” or “non-flight deck effect” fault. Since there’s no immediate flight deck effect, it won’t trigger an alert on the Engine Indicating and Crew Alerting System (EICAS) but will be recorded for maintenance review.

3. **In order to control and see the CMCF, what are the options?**  
   The CMCF can be accessed and controlled via the Maintenance Access Terminal (MAT) on the flight deck, typically through a multifunction display (MFD) or a dedicated maintenance laptop connected to the aircraft’s data network. Authorized personnel use these interfaces to view fault logs, run diagnostic tests, and manage system data.

4. **Some of the alerts logically prevented during landing to prevent the crew being distracted. What signals are used to prevent the alerts in the DCAF?**  
   The Data Concentrator and Alerting Function (DCAF) uses signals such as weight-on-wheels (WOW), airspeed, altitude, and landing gear position to inhibit non-critical alerts during landing. These signals ensure that only critical warnings (e.g., imminent safety issues) are presented to the crew during high-workload phases.

5. **A Cursor Control Device works on which displays?**  
   The Cursor Control Device (CCD) operates on the multifunction displays (MFDs) and the lower center display on the flight deck. It allows pilots to interact with menus, charts, and system interfaces displayed on these screens.

6. **Normally where can the EICAS be seen?**  
   The Engine Indicating and Crew Alerting System (EICAS) is normally displayed on the center multifunction displays (MFDs) of the flight deck, specifically the upper and lower center screens, depending on the configuration selected by the crew.

7. **What is the maximum number of manual and auto event snapshots that can be stored?**  
   The 787’s CMCF can typically store up to 50 manual event snapshots and 50 automatic event snapshots, though this number may vary slightly based on software configuration. These snapshots capture system data during specific fault events for later analysis.

