# Capture the Flag 2025

This repo contains solutions to some of the challenges that are included in the 6th part of **Cyber Security Base 2025** course organized by University of Helsinki, Department of Computer Science. The course was held between Autumn 2025 and Spring 2026.

## <span style="color:white; background-color: green; border: 3px solid black;">&nbsp;&nbsp;&nbsp;</span> Easy challenges


### Oh my nerves! -- CAPTURED

#### Description:
Where is Lydia? Last time I saw her she was talking to Mr. Wickham. Now I can only find this [image] in her room.

#### Solution:
In this challenge, an image file `flower.jpg` was provided.

I opened the image file in Notepad++. A hex editor would be good too. I scrolled down to the very end of the file to find a string "*LetsElopeTogether*". [See solution](1_01_Oh_my_nerves_CAPTURED/solution.png).

### Music box -- CAPTURED

#### Description:
Kitty and Lydia locked Mary's piano notes behind a [password]. Can you help her out?

#### Solution:
In this challenge, a file `box` was provided.

I opened the file in Notepad++. A hex editor would be good too.  I scrolled down the file to find a string "*Password, please:  %255s PlaySomethingNiceMary Correct Incorrect*". [See solution](1_02_Music_box/solution.png)

### Netherfield Ball -- CAPTURED

#### Description:
Mrs. Bennet forgot her passkey needed to attend Netherfield Ball. Please help her, or her daughters will miss the biggest event of the year!

#### Solution:
In this challenge, a link to a webpage was provided. In the webpage,  there was a text field in which the passkey would be inserted.

I opened the webpage to see it's source HTML. At the end of the HTML, there was a link to an external JavaScript file `test.js`. I opened the file and scrolled down to find the following:

```javascript
function x(e) {if (e.target.value == "MrBennet!") {s.textContent = "Valid password!"} else {s.textContent = "Invalid password!"}}
```

[See solution](1_03_Netherfield_Ball/solution.png)

### Gossip -- CAPTURED

#### Description:
Louisa and Carolina like to gossip using XOR and a one-time pads. You find out that the Louisa sends a plain text message 'Bennet' encrypted as [61, 162, 209, 128, 174, 97]. Carolina sends a reply [44, 168, 243, 129, 190, 113], and arrogantly reuses the pad. Decrypt the message.

#### Solution:
First, I converted the plain text message 'Bennet' into binary form. Then I did the same thing to the encrypted message [61, 162, 209, 128, 174, 97]. Since the encrypted message was the result of an XOR operation, I managed to get the key as the second factor of the XOR operation.

Then I converted the encrypted reply message [44, 168, 243, 129, 190, 113] into binary form and decrypted the message with XOR operation using the key I got from previous step. 

Finally, I converted to the resulting binary string into text string **SoLoud**.

### Mr. Darcy's secret -- CAPTURED

#### Description:
It is a truth universally acknowledged, that a man in possession of a good fortune, must be in want of a public-private cryptosystem. Mr. Darcy has chosen his RSA modulus n=1829, and a public key e=83. He receives a cipher 1151 that has been encrypted with her public key. What is the plaintext?

#### Solution:
Here I wrote a tiny python code snippet for small brute-forcing in order to find out the original message since the encypted message and all the necessary attributes for the encyption were given.

I knew the original message was in numeric form so I gave a small enough range for the snippet to go through in order to calculate which original message would give a cipher 1151.

```python
def encrypted(msg, e=83, n=1829):
    return (msg**e) % n

def main():
    for msg in range(1, 1000):
        e_msg = encrypted(msg)
        if e_msg == 1151:
            print(f"Msg: {msg} ==> {e_msg}")
```

The code snippet gave **419** as the original message.

[See solution](1_05_Mr._Darcy's_secret/solution.png)

### Mr. Hurst -- CAPTURED

#### Description:
Mr. Hurst wrote a message in his stupor, and now, when somber, doesn't remember what he was doing. Can you help him to remember:
*D ndhkgt yji'o piyzmnoviy rct Zgduvwzoc Wziizo yjzni'o rvio oj kgvt vit xvmy bvhzn. Di vit xvnz, D avixt htnzga v bvhz ja Gviozmgjj.*

#### Solution:
This was a simple case of Caesar cipher, so it didn't take too long to decipher the message:
**I simply don't understand why Elizabeth Bennet doesn't want to play any card games. In any case, I fancy myself a game of Lanterloo.**

In this challenge it was a bit unclear what was the desired answer, but in the end it was a single word from the deciphered message and in this case **Lanterloo**.

### Logs logs logs

### Bank I

### Bank II -- CAPTURED

#### Description:
The main page of Lambton Bank does some curious AJAX calls. Can you find the key?

#### Solution:
In this challenge, a link to a webpage was provided.

Using Google Chrome, I opened Developer Tools switching to *Network* tab where I saw that a file `token.json` was fetched. I opened the .json file to find the following key-value pair:

`backend-key:  "SwimminginaLake"`

[See solution](1_09_Bank_II/solution.png)

### Mr. Wickham's debts

## <span style="color:white; background-color: gold; border: 3px solid black;">&nbsp;&nbsp;&nbsp;</span> Medium challenges

## <span style="color:white; background-color: red; border: 3px solid black;">&nbsp;&nbsp;&nbsp;</span> Hard challenges
