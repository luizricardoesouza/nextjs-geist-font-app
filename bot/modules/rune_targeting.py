import time
import random
import pyautogui
from utils import config, logger

class RuneTargeting:
    def __init__(self):
        self.logger = logger.logger
        self.is_active = False
        self.last_use = 0
        self.cooldown = 1.0  # 1 second cooldown between rune uses

    def use_rune_on_target(self, target_pos):
        """
        Use rune on a specific target position
        Args:
            target_pos: tuple (x, y) of target position on screen
        """
        try:
            current_time = time.time()
            if current_time - self.last_use < self.cooldown:
                return False

            # Press the configured rune hotkey
            pyautogui.press(config.KEY_BINDINGS["use_rune"])
            
            # Add random delay before clicking (more human-like)
            time.sleep(random.uniform(
                config.RUNE_CONFIG["target_delay_min"],
                config.RUNE_CONFIG["target_delay_max"]
            ))
            
            # Move mouse to target and click
            pyautogui.click(x=target_pos[0], y=target_pos[1])
            
            self.last_use = current_time
            self.logger.debug(f"Used rune on target at position {target_pos}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error using rune on target: {e}", exc_info=True)
            return False

    def toggle(self):
        """Toggle rune targeting on/off"""
        self.is_active = not self.is_active
        self.logger.info(f"Rune targeting {'enabled' if self.is_active else 'disabled'}")

    def handle_hotkey(self):
        """
        Handle the rune hotkey press
        Should be called when the configured rune hotkey is pressed
        """
        if self.is_active:
            # Get current mouse position as target
            x, y = pyautogui.position()
            self.use_rune_on_target((x, y))
