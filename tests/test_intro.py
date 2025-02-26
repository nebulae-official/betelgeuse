from intro.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr().out.strip()
    assert captured == "Welcome to Betelgeuse! This is your introduction script."
