# Tibia 7.4 Bot

A Python-based bot for Tibia 7.4 with features including cave bot, auto targeting, spell attacks, healing, and rune making/targeting.

## Features

- **Cave Bot**: Automated cave navigation using waypoints
- **Auto Target**: Automatic monster detection and targeting
- **Spells Attack**: Automated spell casting
- **Healing System**: Auto-healing using spells and runes
- **Rune Making**: Automated rune creation
- **Rune Targeting**: Quick rune usage with configurable hotkey

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit the settings in `utils/config.py` to customize:
- Hotkeys
- Waypoints
- Healing thresholds
- Delays and timings

Default hotkeys:
- `F` - Use rune on target
- `Ctrl + F` - Toggle rune targeting mode
- `Ctrl + T` - Toggle auto targeting
- `Ctrl + Q` - Stop bot

## Usage

1. Start the bot:
```bash
python main.py
```

2. Controls:
- Press the configured rune hotkey (default: 'F') to use rune on current target
- Hold Ctrl + rune hotkey to toggle rune targeting mode
- Use Ctrl + T to toggle auto targeting
- Use Ctrl + Q to stop the bot

## Safety Features

- Random delays between actions
- Human-like mouse movements
- Configurable cooldowns
- Error handling and logging

## Logging

Logs are stored in the `logs` directory with timestamps. Check these logs for:
- Bot activity
- Error messages
- Debug information

## Warning

Using bots in Tibia may violate the game's terms of service. Use at your own risk.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
