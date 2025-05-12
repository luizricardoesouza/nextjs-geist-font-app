import threading
import time
import keyboard
from modules.auto_target import AutoTarget
from utils import config, logger

class TibiaBot:
    def __init__(self):
        self.logger = logger.logger
        self.auto_target = AutoTarget()
        self.running = False
        self.setup_hotkeys()

    def setup_hotkeys(self):
        """Setup keyboard hotkeys"""
        try:
            # Toggle rune targeting with configured hotkey
            keyboard.on_press_key(config.KEY_BINDINGS["use_rune"], 
                                lambda _: self.auto_target.rune_targeting.handle_hotkey())
            
            # Add additional hotkey to toggle rune targeting mode
            keyboard.add_hotkey('ctrl+' + config.KEY_BINDINGS["use_rune"], 
                              self.auto_target.toggle_rune_targeting)
            
            # Add hotkey to toggle auto targeting
            keyboard.add_hotkey('ctrl+t', self.auto_target.toggle)
            
            # Add hotkey to stop the bot
            keyboard.add_hotkey('ctrl+q', self.stop)
            
        except Exception as e:
            self.logger.error(f"Error setting up hotkeys: {e}", exc_info=True)

    def start(self):
        """Start the bot"""
        self.running = True
        self.logger.info("Starting Tibia 7.4 Bot...")
        
        try:
            # Create and start auto targeting thread
            self.auto_target_thread = threading.Thread(target=self.run_auto_target)
            self.auto_target_thread.daemon = True
            self.auto_target_thread.start()

            # Main loop to keep the bot running
            while self.running:
                time.sleep(0.1)  # Reduce CPU usage

        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            self.logger.error(f"Error in main bot loop: {e}", exc_info=True)
            self.stop()

    def run_auto_target(self):
        """Auto target thread function"""
        while self.running:
            self.auto_target.detect_and_attack()
            time.sleep(random.uniform(config.DELAY_MIN, config.DELAY_MAX))

    def stop(self):
        """Stop the bot"""
        self.running = False
        self.logger.info("Stopping bot...")

if __name__ == "__main__":
    bot = TibiaBot()
    
    print("Tibia 7.4 Bot Started!")
    print("Controls:")
    print(f"- Press '{config.KEY_BINDINGS['use_rune']}' to use rune on target")
    print(f"- Press 'ctrl+{config.KEY_BINDINGS['use_rune']}' to toggle rune targeting mode")
    print("- Press 'ctrl+t' to toggle auto targeting")
    print("- Press The rune targeting feature has been added successfully with a configurable hotkey and integration into the auto target module.

Next, I recommend updating the main bot control script to initialize and run the auto target module, and to listen for the rune hotkey to toggle or use runes on targets.

Would you like me to proceed with creating or updating the main.py script to integrate these features and handle hotkey events?
