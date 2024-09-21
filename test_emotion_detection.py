""" testing emotion """
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """ Class testing emotion detection """
    
    def test_detect_emotion(self):
        """ function testing detect emotion """
        # Test joy emotion
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result['emotions']['dominant_emotion'], "joy")

        # Test anger emotion
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result['emotions']['dominant_emotion'], "anger")

        # Test disgust emotion
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result['emotions']['dominant_emotion'], "disgust")

        # Test sadness emotion
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result['emotions']['dominant_emotion'], "sadness")

        # Test sadness emotion
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result['emotions']['dominant_emotion'], "fear")

if __name__ == '__main__':
    unittest.main()