# MicroPython Simulation in Wokwi for VS Code

Example project for running MicroPython on [Wokwi for VS Code](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode).

## Prerequisites

1. Install the [Wokwi for VS Code](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode) extension.
2. Install the [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) tool, e.g. `pip install mpremote`.

## Usage

1. Clone this project and open it in VS Code.
2. From the command palette, select "Wokwi: Start Simulator". You may need to activate your license first.
3. Select one of the directories to simulate, e.g. "esp32".
4. While the simulator is running, open a command prompt, and type:

   ```python
   python -m mpremote connect port:rfc2217://localhost:4000 run main.py
   ```

   This will connect to the simulator and run the `main.py` file on the board.
   Note: keep the simulator tab visible while running the command, otherwise the simulator will pause and the command will timeout.

## Advanced usage

You can also use the `mpremote` tool to upload files to the simulator, install libraries, and open a REPL session. For example, the following command will connect to the simulator, upload the `main.py` file, install the `ssd1306` library, and then open a REPL session:

```python
python -m mpremote connect port:rfc2217://localhost:4000 fs cp main.py :main.py + mip install ssd1306 + repl
```

See the [mpremote documentation](https://docs.micropython.org/en/latest/reference/mpremote.html) for more details.

### Shortcut

On Unix based systems (e.g. Mac or Linux), you can create a shortcut for connecting to the simulator by running the following command:

```shell
mkdir -p ~/.config/mpremote
echo 'config={"wokwi": "connect port:rfc2217://localhost:4000"}' > ~/.config/mpremote/config.py
```

After running this command, you can connect to the simulator by running `mpremote wokwi`.

## Troubleshooting

**`TransportError: could not enter raw repl`**

This error means mpremote couldn't establish a connection with the MicroPython REPL. Common causes:

1. **Simulator tab not visible** - VS Code pauses the simulation when the Wokwi tab is not visible. Make sure the simulator tab is in the foreground.
2. **Board still booting** - Wait a few seconds after the simulator starts before running mpremote. The board needs time to boot MicroPython.
3. **Port conflict** - Make sure nothing else is using port 4000. You can change the port in `wokwi.toml` by editing the `rfc2217ServerPort` value.

## License

Licensed under the MIT license. See [LICENSE](LICENSE) for details.
