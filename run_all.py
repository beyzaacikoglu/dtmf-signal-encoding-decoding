import argparse
import subprocess
import sys
import os


def run_script(path, input_text=None):
    python = sys.executable
    cwd = os.path.dirname(__file__) or os.getcwd()
    full_path = os.path.join(cwd, path)
    if input_text is not None:
        return subprocess.run([python, full_path], input=(input_text + "\n").encode(), cwd=cwd).returncode
    else:
        return subprocess.run([python, full_path], cwd=cwd).returncode


def main():
    parser = argparse.ArgumentParser(description="Run encode, decode and plots in one command")
    parser.add_argument('-t', '--text', help='Text to encode; if omitted, encoder will prompt')
    args = parser.parse_args()

    print("1/3 — Running encoder")
    rc = run_script('dtmf_encode.py', input_text=args.text)
    if rc != 0:
        print('Encoder failed with code', rc)
        sys.exit(rc)

    print("2/3 — Running decoder")
    rc = run_script('dtmf_decode.py')
    if rc != 0:
        print('Decoder failed with code', rc)
        sys.exit(rc)

    print("3/3 — Generating plots")
    rc = run_script('plots.py')
    if rc != 0:
        print('Plots script failed with code', rc)
        sys.exit(rc)

    print('All done. encoded.wav, zaman_domeni.png and fft.png created.')


if __name__ == '__main__':
    main()
