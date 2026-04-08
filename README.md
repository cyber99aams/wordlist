# Wordlist Collection

এই রিপোজিটরিতে বিভিন্ন ধরণের সিকিউরিটি টেস্টিং 
এবং রিসার্চের জন্য প্রয়োজনীয় ওয়ার্ডলিস্ট এবং জেনারেটর টুলস রয়েছে।

## সূচিপত্র (Contents)

- **Digit Wordlists:** ৪, ৫, এবং ৬ ডিজিটের কম্বিনেশন ফাইল।
- **Name Lists:** নামের তালিকা (f-name.txt, m-name.txt)।
- **Python Scripts:** - `digit-generator.py`: কাস্টম ডিজিট লিস্ট তৈরির জন্য।
    - `user-generator.py`: ইউজারনেম তৈরির জন্য।
- **Others:** `hotspass.txt` এবং `rockyou.txt` (Release সেকশনে উপলব্ধ)।

## ডাউনলোড এবং ব্যবহার (Usage)

রিপোজিটরি ক্লোন করতে নিচের কমান্ডটি ব্যবহার করুন:

```
git clone https://github.com/cyber99aams/wordlist.git
cd wordlist
```
```
wget https://github.com/cyber99aams/wordlist/releases/download/v3.0/rockyou.txt
mv rockyou.txt wordlist
```
**স্ক্রিপ্ট চালানোর নিয়ম**

`python digit-generator.py`

`python user-generator.py`

## Disclaimer:
**এই ওয়ার্ডলিস্টগুলো শুধুমাত্র শিক্ষামূলক
এবং বৈধ সিকিউরিটি অডিটিং কাজের জন্য তৈরি করা হয়েছে।
কোনো অনৈতিক কাজে এর ব্যবহারের জন্য ডেভেলপার দায়ী থাকবে না।**
