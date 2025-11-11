thonimport json
from extractors.youtube_parser import extract_transcripts
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def main():
    # Load settings
    settings = SETTINGS

    # Sample channel URL to extract
    channel_url = "https://www.youtube.com/channel/UCTgwcoeGGKmZ3zzCXN2qo_A"
    
    # Extract transcripts from channel
    transcripts = extract_transcripts(channel_url, settings)

    # Export transcripts to JSON
    export_to_json(transcripts, "output_transcripts.json")

if __name__ == "__main__":
    main()