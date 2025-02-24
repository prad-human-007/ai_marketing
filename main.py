import argparse
from youtube_api import youtube_search, add_comment
from utils import setup_logger

logger = setup_logger('main', 'main.log')

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Search and Comment Tool')
    parser.add_argument('query', type=str, nargs='?', default='Visa Preparation for US Visa', help='Search query for YouTube videos')
    parser.add_argument('comment', type=str, nargs='?', default="This is a great tool visaprepai", help='Comment to add to the videos')
    parser.add_argument('--max_results', type=int, default=1, help='Maximum number of videos to search (default: 5)')

    query = 'Visa Preparation for US Visa'
    comment = "This is a great tool visaprepai"
    
    args = parser.parse_args()

    try:
        video_ids = youtube_search(query, args.max_results)
        logger.info(f"Found videos: {video_ids}")

        if video_ids:
            for video_id in video_ids:
                add_comment(video_id, comment)
                logger.info(f"Added comment to video {video_id}")
        else:
            logger.info("No videos found.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()