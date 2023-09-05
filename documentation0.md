NOTE: THIS IS TO BE MOVED ELSEWHERE!

Project 0 - Setting Up Git for Seamless File Management

Problem:

Back in school, managing our files could be a precarious endeavor. Individual accounts and cloud storage had their limitations, and the threat of losing non-storage files due to unexpected events or security breaches was always looming. This became especially evident when a few classmates decided to venture into hacking the school's inner network, prompting increased vigilance from teachers and frequent computer wipes. This led me to the realization that I needed a reliable way to keep my files updated seamlessly.

Additionally, the significance of Git and GitHub in the world of IT couldn't be ignored. So, I made the decision to maintain an up-to-date GitHub account, housing my essential files related to Linux, Programming, and Networks.

Steps:

    Initialize Git Repository:
        On my primary Linux machine, I started by creating the appropriate folders and initializing an empty Git repository using the command git init.

    Connect to GitHub:
        I then linked this repository to my GitHub account using the command git remote add origin git@github.com:myusername/my-repo.git.

    Generate SSH Keys:
        To ensure secure access, I generated SSH keys with the command ssh-keygen -t rsa -b 4096 -C "my_email@example.com". I saved the keys to a location of my choice and set a password for added security.

    Add SSH Key to SSH-agent:
        Next, I added the SSH key to the SSH-agent using the commands eval "$(ssh-agent -s)" (which returned the agent PID) and ssh-add ~/.ssh/id_rsa (where I re-entered the password).

    Add SSH Key to GitHub Account:
        To complete the setup, I copied the SSH key to my GitHub account. I navigated to 'Profile Pic' in the upper right corner > 'Settings' > 'SSH and GPG keys' > 'New SSH Key'. I gave it a memorable name and pasted the key (previously copied with cat ~/.ssh/id_rsa.pub | xsel --clipboard. You can use pbcopy < ~/.ssh/id_rsa.pub, if you are on a mac, or type C:\Users\MyUsername\.ssh\id_rsa.pub | clip, if working on a windows computer).

    Ready to Work with Git:
        With these steps done, I was ready to start working with Git. Commands like git add ., git commit -m "commit message", git push origin master, and git pull origin master became my allies. I could also check the status of my files with git status.

    Why SSH?
        I opted for SSH over tokens because it proved to be more convenient. With SSH, I only needed a private key for each machine and a single public key. This simplicity and the added benefit of mastering SSH made it a clear choice.
Do remember, though, that SSH is connected to your GitHub account (not to specific repositories).

    Ongoing Use:
        From then on, every time I made changes to my files within the Git folder, I simply added them, committed them, and pushed them to GitHub. Git and GitHub were now powerful tools enhancing my IT work.

    A good idea:
	Why not add a passphrase to your Private SSH hey? This will add an extra layer of protection to your repositories. You can do that with ssh-keygen -p -f ~/.ssh/id_rsa (don't forget to add the SSH key with the passphrase to the SSH agent with ssh-add ~/.ssh/id_rsa). You'll be prompted for the passphrase at the start of your session, and won't probably be asked for it during that same session.
 
Adding Another Computer:

    When introducing a new computer to this setup, I followed these steps:

    Identify SSH Key:
        First, I identified the correct SSH key on my original computer using ls -al ~/.ssh.

    Copy Key Pair:
        I copied the key pair to a secure location for transfer, such as a USB drive.

    Transfer to New Computer:
        I then copied the key pair files from the USB drive to the new computer's ~/.ssh/ directory using cp /path/to/my/usb/drive/id_mykey* ~/.ssh/.

    Set Permissions:
        It's crucial not to forget to set the correct permissions on the key pair with chmod 600 ~/.ssh/id_mykey.

    This allowed me to use the same key pair on the new machine, ensuring seamless access. Note that you can repeat this process for each new machine or choose to have distinct key pairs for each one, depending on your preference.

Removal:

    If, at any point, you decide to remove the SSH key, Git repository, or associated folder, follow these steps:

    Check SSH Keys:
        Verify which SSH keys are present in your system with ssh-add -l. Copy the fingerprint for reference.

    Delete SSH Key from GitHub:
        Go to your GitHub account and delete the corresponding SSH key. Ensure you select the correct one by comparing fingerprints.

    Remove Local Git Repository:
        To remove the local Git repository, navigate to the respective folder and execute rm -rf .git. This command will delete all .git files within that directory.

    Optional: Delete Folder:
        If desired, you can now delete the folder.

By following these steps, you can easily manage your files and access them across multiple devices while maintaining the security and simplicity of SSH key authentication. Happy experimenting with Git and GitHub, two indispensable tools for anyone working in IT!
