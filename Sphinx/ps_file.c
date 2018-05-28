#include <pocketsphinx.h>
#include <string.h>

int main(int argc, char *argv[])
{
    ps_decoder_t *ps;
    cmd_ln_t *config;
    FILE *fh;
    char const *hyp, *uttid;
    int16 buf[512];
    int rv;
    int32 score;

	    again:

    config = cmd_ln_init(NULL, ps_args(), TRUE,
		         "-hmm", MODELDIR "/en-us/en-us",
		         "-lm", "/var/www/sphinx/j.lm",
	    		 "-dict", "/var/www/sphinx/j.dic",
		         NULL);
    if (config == NULL) {
	fprintf(stderr, "Failed to create config object, see log for details\n");
	return -1;
    }

    ps = ps_init(config);
    if (ps == NULL) {
	fprintf(stderr, "Failed to create recognizer, see log for details\n");
	return -1;
    }

    fh = fopen("ps_file.raw", "rb");
    if (fh == NULL) {
	fprintf(stderr, "Unable to open input file goforward.raw\n");
	return -1;
    }

    rv = ps_start_utt(ps);

    while (!feof(fh)) {
	size_t nsamp;
	nsamp = fread(buf, 2, 512, fh);
	rv = ps_process_raw(ps, buf, nsamp, FALSE, FALSE);
    }

    rv = ps_end_utt(ps);
    hyp = ps_get_hyp(ps, &score);

    printf("%s\n", hyp);
/*
    int rescmp = strcmp(hyp, "JARVICE");

    if (!rescmp) {
        printf("Detected!\n"); 
	fclose(fh);
        ps_free(ps);
        cmd_ln_free_r(config);

	return 1;
    }
    else {
        fclose(fh);
        ps_free(ps);
        cmd_ln_free_r(config);
	
        return rescmp;
    }
*/
    return 0;
}


















