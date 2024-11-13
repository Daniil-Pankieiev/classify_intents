import json
import logging
from utils.csv_processor import decode_base64_csv
from utils.similarity import get_top_similar_sentences

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    if 'body' not in event:
        return {'statusCode': 400, 'body': json.dumps({'error': 'No body in the request'})}

    try:
        # Parse JSON body
        body = json.loads(event['body'])
        phrase = body['phrase']
        intents_file_base64 = body['intents']

        # Decode and process CSV file
        intents_data = decode_base64_csv(intents_file_base64)

        # Get descriptions to calculate similarity
        sentences = intents_data['Description'].tolist()
        # Get top 3 similar descriptions
        top_similar_sentences = get_top_similar_sentences(phrase, sentences, top_n=3)
        # Map top similar descriptions to intents
        top_intents = []
        for description, score in top_similar_sentences:
            intent = intents_data.loc[intents_data['Description'] == description, 'Intent'].values[0]
            top_intents.append(intent)

        logger.info(f"Classified intents: {top_intents}")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

    return {
        'statusCode': 200,
        'body': json.dumps({'categories': top_intents})
    }
