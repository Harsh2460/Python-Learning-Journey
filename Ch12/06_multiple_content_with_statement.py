with (
    open("file1.txt","w") as f1,
    open("file2.txt","w") as f2
):
    # Prcoess File

    f1.write("Good Morning")
    f2.write("Good Night")