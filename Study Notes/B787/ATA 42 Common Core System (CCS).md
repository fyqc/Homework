Quiz questions regarding the Boeing 787's ATA 42 Common Core System (CCS):

1. **What are components found in the CCR?**  
   The Common Computing Resource (CCR) cabinets contain:  
   - General Processor Modules (GPMs) for running hosted software applications.  
   - Power Conditioning Modules (PCMs) for power supply and regulation.  
   - Fiber Optic Translator (FOX) Modules for converting electrical signals to optical signals and vice versa.  
   - ARINC 664 Network Cabinet Switches (ACS) for network communication.

2. **What is the primary purpose of the CCR?**  
   The primary purpose of the CCR is to provide a centralized computing platform that hosts software applications for various airplane systems, offering processing, power, and network connectivity while reducing weight, cost, and the number of standalone units.

3. **How many CCRs are there and where do they get their power from?**  
   There are two CCRs on the Boeing 787: a Left CCR and a Right CCR. They receive power from the airplane’s electrical system, primarily through the Hot Battery Bus, which is backed up by the main battery and other power sources like generators or the APU depending on the operational mode.

4. **Hot Batt Bus power is supplied to both CCRs from?**  
   The Hot Battery Bus power is supplied to both CCRs from the main battery, located in the forward electronics equipment (E/E) bay, ensuring continuous power availability even during startup or backup scenarios.

5. **The hosted software applications for airplane system are found in the?**  
   The hosted software applications for airplane systems are found in the General Processor Modules (GPMs) within the CCR cabinets, where they run in a partitioned environment to support various aircraft functions.

6. **What changes light signals to electrical and vice versa?**  
   The Fiber Optic Translator (FOX) Modules change light (optical) signals to electrical signals and vice versa, facilitating communication over the fiber optic network.

7. **The ACS (ARINC 664 Network Cabinet Switches) have how many channels and what they?**  
   The ARINC 664 Network Cabinet Switches (ACS) have two channels: Channel A and Channel B. These channels provide redundant, high-speed data communication pathways within the Common Data Network (CDN) using the ARINC 664 protocol.

8. **The ARS (ARINC 664 Remote Switches) connect the airplane systems through ______ and what component?**  
   The ARINC 664 Remote Switches (ARS) connect airplane systems through copper or fiber optic ports to the Remote Data Concentrators (RDCs), enabling data exchange between the CDN and systems not directly using ARINC 664.

9. **Which types of connections do the RDC (Remote Data Concentrators) have?**  
   The Remote Data Concentrators (RDCs) have the following types of connections:  
   - ARINC 429 (high and low speed).  
   - Controller Area Network (CAN) bus.  
   - Analog signals.  
   - Analog discrete signals.  
   These allow RDCs to interface legacy or non-ARINC 664 systems with the CDN.

10. **During the inhibited mode what causes the CCS to start up?**  
   During the inhibited mode, the CCS starts up when any of these conditions occur: the airplane is in the air, any fuel switch is on, or fuel switch data is lost, triggering a rapid boot-up process without a full built-in test.

11. **How long does it take for the CCS to power-up on battery?**  
   When powered up on battery only, the CCS takes approximately 50 seconds to become operational, with displays becoming available after this time in inhibited mode.

12. **When displays blank in flight, how can the flight crew possibly recover and how long does it take?**  
   If displays blank in flight, the flight crew can attempt recovery by pressing the Left or Right CCR reset switch on the overhead panel, which resets power to the respective CCR cabinet’s modules. Recovery time depends on the issue, but in inhibited mode, the system can be ready in about 50 seconds; however, a full resolution might require more time or a complete power cycle if the fault persists.

13. **Some components do not have direct connections with the CDN. Where can you see the status of these connections?**  
   The status of components not directly connected to the Common Data Network (CDN), such as those interfaced via RDCs, can be viewed on the CCS maintenance pages (e.g., pages 7 and 8) on the flight deck displays, which show RDC and switch statuses, or through the Central Maintenance Computing Function (CMCF) for detailed fault logging.

These answers are based on the Boeing 787’s Common Core System architecture, focusing on its components, functionality, and operational behavior as of March 19, 2025. 
