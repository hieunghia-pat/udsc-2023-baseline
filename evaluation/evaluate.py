import re
import unicodedata

def preprocess_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"['\",\.\?:\-!()/]", "", text)
    text = text.strip()
    text = " ".join(text.split())
    text = text.lower()
    return text

def strict_accuracy(gt: dict, pred: dict) -> dict:
    gt_verdict = gt["verdict"]
    pred_verdict = pred["verdict"]
    gt_evidence = gt["evidence"]
    pred_evidence = pred["evidence"]

    gt_evidence = preprocess_text(gt_evidence)
    pred_evidence = preprocess_text(pred_evidence)

    acc = int(gt_verdict == pred_verdict)
    acc_1 = int(gt_evidence == pred_evidence)
    strict_acc = acc * acc_1

    return {
        "strict_acc": strict_acc,
        "acc": acc,
        "acc@1": acc_1,
    }

