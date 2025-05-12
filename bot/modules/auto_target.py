import time
import random
import pyautogui
from utils import config, logger
from .rune_targeting import RuneTargeting

class AutoTarget:
    def __init__(self):
        self.logger = logger.logger
        self.rune_targeting = RuneTargeting()
        self.last_target_pos = None
        self.is_active = True

    def detect_target(self):
        """
        Detect potential target on screen
        Returns:
            tuple: (x, y) coordinates of target if found, None otherwise
        """
        try:
            # Here you would implement actual target detection logic
            # This could involve screen capture and image processing
            # For now, we'll use a dummy implementation
            
            # Simulate finding a target at a random position
            # In real implementation, this would be replaced with actual detection
            x = random.randint(100, 800)
            y = random.randint(100, 600)
            return (x, y)
            
        except Exception as e:
            self.logger.error(f"Error detecting target: {e}", exc_info=True)
            return None

    def attack_target(self, target_pos):
        """
        Attack detected target using configured attack method
        """
        try:
            if not target_pos:
                return False

            self.last_target_pos = target_pos
            
            # Use normal attack
            pyautogui.press(config.KEY_BINDINGS["attack_spell"])
            time.sleep(random.uniform(config.DELAY_MIN, config.DELAY_MAX))
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error attacking target: {e}", exc_info=True)
            return False

    def use_rune_if_active(self):
        """
        Use rune on last known target if rune targeting is active
        """
        if self.rune_targeting.is_active and self.last_target_pos:
            return self.rune_targeting.use_rune_on_target(self.last_target_pos)
        return False

    def toggle(self):
        """Toggle auto targeting on/off"""
        self.is_active = not self.is_active
        self.logger.info(f"Auto targeting {'enabled' if self.is_active else 'disabled'}")

    def detect_and_attack(self):
        """
        Main method to detect and attack targets
        """
        if not self.is_active:
            return

        self.logger.info("Auto target activated...")
        try:
            target_pos = self.detect_target()
            if target_pos:
                self.attack_target(target_pos)
                # If rune targeting is active, use rune after attack
                self.use_rune_if_active()
                
        except Exception as e:
            self.logger.error(f"Error in auto target module: {e}", exc_info=True)

    def toggle_rune_targeting(self):
        """Toggle rune targeting feature"""
        self.rune_targeting.toggle()
