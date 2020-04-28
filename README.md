# InputSharer
Share Keyboard and Mouse Input between Two Computers

## Usage
The current implementation assumes that the sender is a Mac, and the receiver is a windows PC. But this could be easily changed, by modifying the build_key_code_map logic in the receiver code.

On the receiver, run "python receiver.py"

On the sender, run "python3 {receiver id+port}"
